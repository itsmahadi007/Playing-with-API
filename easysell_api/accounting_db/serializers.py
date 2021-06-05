from rest_framework import serializers
from .models import *


class testDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = testdb
        fields = "__all__"


class customer_listSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer_list
        fields = "__all__"


class inventory_add_readystockSerializer(serializers.ModelSerializer):
    class Meta:
        model = inventory_add_readystock
        fields = "__all__"


class inventory_add_rowstockSerializer(serializers.ModelSerializer):
    class Meta:
        model = inventory_add_rowstock
        fields = "__all__"


class inventory_production_child_receipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = inventory_production_child_receipe
        fields = "__all__"


class inventory_production_root_receipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = inventory_production_root_receipe
        fields = "__all__"


class m_expenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = m_expense
        fields = "__all__"


class paymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = payments
        fields = "__all__"


class s_expenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = s_expense
        fields = "__all__"


class serial_keySerializer(serializers.ModelSerializer):
    class Meta:
        model = serial_key
        fields = "__all__"


class sold_child_tableSerializer(serializers.ModelSerializer):
    class Meta:
        model = sold_child_table
        fields = "__all__"


class sold_child_table_posSerializer(serializers.ModelSerializer):
    class Meta:
        model = sold_child_table_pos
        fields = "__all__"


class sold_root_tableSerializer(serializers.ModelSerializer):
    class Meta:
        model = sold_root_table
        fields = "__all__"


class sold_root_table_posSerializer(serializers.ModelSerializer):
    class Meta:
        model = sold_root_table_pos
        fields = "__all__"


class temp_inventory_production_child_receipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = temp_inventory_production_child_receipe
        fields = "__all__"


class temp_saleSerializer(serializers.ModelSerializer):
    class Meta:
        model = temp_sale
        fields = "__all__"


class temp_sale_posSerializer(serializers.ModelSerializer):
    class Meta:
        model = temp_sale_pos
        fields = "__all__"


class theme_colorSerializer(serializers.ModelSerializer):
    class Meta:
        model = theme_color
        fields = "__all__"


class trial_period_calculateSerializer(serializers.ModelSerializer):
    class Meta:
        model = trial_period_calculate
        fields = "__all__"


class useracSerializer(serializers.ModelSerializer):
    class Meta:
        model = userac
        fields = "__all__"


class v_expenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = v_expense
        fields = "__all__"


class vendor_listSerializer(serializers.ModelSerializer):
    class Meta:
        model = vendor_list
        fields = "__all__"


class vendor_list_readyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = vendor_list_readyProduct
        fields = "__all__"


class vendor_list_rowProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = vendor_list_rowProduct
        fields = "__all__"


class zzz_permanent_valuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = zzz_permanent_values
        fields = "__all__"
