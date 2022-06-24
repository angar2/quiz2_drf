from rest_framework import serializers
from .models import Company as CompanyModel
from .models import JobPost as JobPostModel
from .models import JobPostSkillSet as JobPostSkillSetModel


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyModel
        fields = ["company_name", "business_area"]

class JobPostSkillSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobPostSkillSetModel
        fields = ["skill_set", "job_post"]

class JobPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobPostModel
        fields = ["job_type", "company", "job_description", "salary"]