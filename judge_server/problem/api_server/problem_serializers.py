from rest_framework import serializers
from utils.serializers import resource_read_only

from ..models import Problem

from ..models import Limit
from ..models import TestData, ProblemTestData

from ..tasks import send_data_insert


class ProblemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        exclude = ('test_data',)
        read_only_fields = resource_read_only + ('meta_problem',
                                                 'number_test_data',
                                                 'number_decorator',
                                                 'number_limit',
                                                 'number_category',
                                                 'number_node')

    def create(self, validated_data):
        description = validated_data.get('description')
        sample = validated_data.get('sample')
        meta_problem = validated_data['meta_problem']
        if description is not None and description.meta_problem != meta_problem:
            raise serializers.ValidationError('Cannot choose description from other meta problem.')
        if sample is not None and sample.meta_problem != meta_problem:
            raise serializers.ValidationError('Cannot choose sample from other meta problem.')
        return super().create(validated_data)


class ProblemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'
        read_only_fields = resource_read_only + ('meta_problem',
                                                 'number_test_data',
                                                 'number_decorator',
                                                 'number_limit',
                                                 'number_category',
                                                 'number_node')

    def update(self, instance, validated_data):
        description = validated_data.get('description')
        sample = validated_data.get('sample')
        meta_problem = instance.meta_problem
        if description is not None and description.meta_problem != meta_problem:
            raise serializers.ValidationError('Cannot choose description from other meta problem.')
        if sample is not None and sample.meta_problem != meta_problem:
            raise serializers.ValidationError('Cannot choose sample from other meta problem.')
        return super().update(instance, validated_data)


class ProblemReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        exclude = ('test_data',)


class LimitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Limit
        fields = '__all__'
        read_only_fields = resource_read_only + ('problem',)

    def create(self, validated_data):
        ret = super().create(validated_data)
        send_data_insert.delay(mid=ret.problem.meta_problem_id)
        return ret


class LimitDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Limit
        fields = '__all__'
        read_only_fields = resource_read_only + ('problem',)

    def update(self, instance, validated_data):
        ret = super().update(instance, validated_data)
        send_data_insert.delay(mid=ret.problem.meta_problem_id)
        return ret


class TestDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestData
        fields = '__all__'


class TestDataRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemTestData
        fields = '__all__'
        read_only_fields = resource_read_only + ('problem',)

    def create(self, validated_data):
        test_data = validated_data['test_data']
        problem = validated_data['problem']
        meta_problem = problem.meta_problem
        print(test_data.meta_problem, meta_problem)
        if test_data is not None and test_data.meta_problem != meta_problem:
            raise serializers.ValidationError('Cannot choose test data from other meta problem.')
        if ProblemTestData.objects.filter(problem=problem, test_data=test_data).exists():
            raise serializers.ValidationError('Relation already exists.')
        return super().create(validated_data)
