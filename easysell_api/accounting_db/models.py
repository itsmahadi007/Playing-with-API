from django.db import models

# Create your models here.


class testdb(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()


class customer_list(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=50, null=True)
    mobile_number = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50, null=True)
    customer_address = models.CharField(max_length=50, null=True)
    serial_no = models.IntegerField()
    table_name = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True)
    timedate = models.CharField(max_length=50, null=True)
    amount = models.FloatField(null=True)
    paid = models.FloatField(null=True)
    due = models.FloatField(null=True)

    def __str__(self):
        return self.id


class inventory_add_readystock(models.Model):
    id = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=50)
    p_code = models.IntegerField(null=True)
    p_barcode = models.CharField(max_length=50, null=True)
    net_amount = models.IntegerField(null=True)
    net_amount_type = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    in_stock = models.IntegerField()
    low_alert = models.IntegerField(null=True)
    supply_ppu = models.IntegerField()
    sell_ppu = models.IntegerField(null=True)
    discount = models.IntegerField()
    supplier = models.CharField(max_length=50, null=True)
    tax = models.IntegerField(null=True)
    allow_change_on_edit = models.IntegerField(null=True)
    date = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.id


class inventory_add_rowstock(models.Model):
    id = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=50)
    p_code = models.IntegerField(null=True)
    p_barcode = models.CharField(max_length=50, null=True)
    net_amount = models.IntegerField(null=True)
    net_amount_type = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    in_stock = models.IntegerField()
    low_alert = models.IntegerField(null=True)
    supply_ppu = models.IntegerField()
    sell_ppu = models.IntegerField(null=True)
    discount = models.IntegerField()
    supplier = models.CharField(max_length=50, null=True)
    tax = models.IntegerField()
    allow_change_on_edit = models.IntegerField(null=True)
    date = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.id


class inventory_production_child_receipe(models.Model):
    id = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=50)
    p_code = models.IntegerField(null=True)
    p_barcode = models.IntegerField(null=True)
    quantity = models.IntegerField()
    cost = models.FloatField(max_length=50)
    root_product = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.id


class inventory_production_root_receipe(models.Model):
    id = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=50)
    p_code = models.IntegerField(null=True)
    p_barcode = models.CharField(max_length=50, null=True)
    net_amount = models.IntegerField(null=True)
    net_amount_type = models.CharField(max_length=50)
    product_cost = models.FloatField()
    sell_ppu = models.IntegerField(null=True)

    def __str__(self):
        return self.id


class m_expense(models.Model):
    id = models.IntegerField(primary_key=True)
    e_no = models.IntegerField()
    e_reason = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    amount = models.IntegerField()
    paid = models.IntegerField()
    due = models.IntegerField()
    date = models.CharField(max_length=50)
    e_by = models.CharField(max_length=50, null=True)
    a_by = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.id


class payments(models.Model):
    id = models.IntegerField(primary_key=True)
    serial_no = models.IntegerField()
    reason = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    amount = models.IntegerField()
    paid = models.IntegerField()
    due = models.IntegerField()
    paid_date = models.CharField(max_length=50)
    paid_by = models.CharField(max_length=50, null=True)
    his_number = models.CharField(max_length=50)
    bill_by = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.id


class s_expense(models.Model):
    id = models.IntegerField(primary_key=True)
    e_no = models.IntegerField()
    s_name = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    amount = models.IntegerField()
    paid = models.IntegerField()
    due = models.IntegerField()
    date = models.CharField(max_length=50)
    reason = models.CharField(max_length=50)

    def __str__(self):
        return self.id


class serial_key(models.Model):
    serial_key = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.serial_key


class sold_child_table(models.Model):
    pk_no = models.IntegerField(primary_key=True)
    id = models.IntegerField()
    serial_no = models.IntegerField()
    p_name = models.CharField(max_length=50, null=True)
    qty = models.IntegerField(null=True)
    taka = models.IntegerField(null=True)
    p_code = models.IntegerField(null=True)
    p_rate = models.IntegerField(null=True)
    n_instock = models.IntegerField(null=True)
    p_barcode = models.CharField(max_length=50, null=True)
    p_rate_buy = models.FloatField(null=True)

    def __str__(self):
        return self.pk_no


class sold_child_table_pos(models.Model):
    pk_no = models.IntegerField(primary_key=True)
    id = models.IntegerField()
    serial_no = models.IntegerField()
    p_name = models.CharField(max_length=50, null=True)
    qty = models.IntegerField(null=True)
    taka = models.IntegerField(null=True)
    p_code = models.IntegerField(null=True)
    p_rate = models.IntegerField(null=True)
    n_instock = models.IntegerField(null=True)
    p_barcode = models.CharField(max_length=50, null=True)
    p_rate_buy = models.FloatField(null=True)

    def __str__(self):
        return self.pk_no


class sold_root_table(models.Model):
    id = models.IntegerField(primary_key=True)
    serial_key = models.IntegerField()
    time = models.CharField(max_length=50, null=True)
    date = models.CharField(max_length=50, null=True)
    total_products = models.IntegerField(null=True)
    total_amount = models.FloatField(null=True)
    tax = models.FloatField(null=True)
    tax_amount = models.FloatField(null=True)
    with_tax = models.FloatField(null=True)
    customer_name = models.CharField(max_length=50, null=True)
    customer_number = models.CharField(max_length=50)
    customer_address = models.CharField(max_length=150, null=True)
    paid = models.FloatField(null=True)
    due = models.FloatField(null=True)
    status = models.CharField(max_length=50, null=True)
    company_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.id


class sold_root_table_pos(models.Model):
    id = models.IntegerField(primary_key=True)
    serial_key = models.IntegerField()
    time = models.CharField(max_length=50, null=True)
    date = models.CharField(max_length=50, null=True)
    total_products = models.IntegerField(null=True)
    total_amount = models.FloatField(null=True)
    tax = models.FloatField(null=True)
    tax_amount = models.FloatField(null=True)
    with_tax = models.FloatField(null=True)
    customer_name = models.CharField(max_length=50, null=True)
    customer_number = models.CharField(max_length=50)
    customer_address = models.CharField(max_length=150, null=True)
    paid = models.FloatField(null=True)
    due = models.FloatField(null=True)
    status = models.CharField(max_length=50, null=True)
    company_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.id


class temp_inventory_production_child_receipe(models.Model):
    id = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=50)
    p_code = models.IntegerField(null=True)
    p_barcode = models.CharField(max_length=50, null=True)
    quantity = models.IntegerField()
    cost = models.FloatField()
    root_product = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.id


class temp_sale(models.Model):
    id = models.IntegerField(primary_key=True)
    serial_key = models.IntegerField(null=True)
    p_name = models.CharField(max_length=50, null=True)
    qty = models.IntegerField(null=True)
    taka = models.FloatField(null=True)
    p_code = models.IntegerField(null=True)
    p_rate = models.IntegerField(null=True)
    n_inStock = models.IntegerField(null=True)
    p_barcode = models.CharField(max_length=50, null=True)
    p_name_row = models.CharField(max_length=50, null=True)
    p_rate_buy = models.FloatField(null=True)

    def __str__(self):
        return self.id


class temp_sale_pos(models.Model):
    id = models.IntegerField(primary_key=True)
    serial_key = models.IntegerField(null=True)
    p_name = models.CharField(max_length=50, null=True)
    qty = models.IntegerField(null=True)
    taka = models.FloatField(null=True)
    p_code = models.IntegerField(null=True)
    p_rate = models.IntegerField(null=True)
    n_inStock = models.IntegerField(null=True)
    p_barcode = models.CharField(max_length=50, null=True)
    p_name_row = models.CharField(max_length=50, null=True)
    p_rate_buy = models.FloatField(null=True)

    def __str__(self):
        return self.id


class theme_color(models.Model):
    id = models.IntegerField(primary_key=True)
    theme_color = models.CharField(max_length=50, null=True)
    dv_bg_color = models.CharField(max_length=50, null=True)
    dv_topbar_bg_color = models.CharField(max_length=50, null=True)
    dv_topbar_fg_color = models.CharField(max_length=50, null=True)
    pos_product_color = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.id


class trial_period_calculate(models.Model):
    id = models.IntegerField(primary_key=True)
    trial_expire_date = models.CharField(max_length=50, null=True)
    expired = models.CharField(max_length=5, null=True)
    trial = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.id


class userac(models.Model):
    id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50, null=True)
    Email = models.CharField(max_length=50, null=True)
    Number = models.CharField(max_length=50, null=True)
    Password = models.CharField(max_length=50, null=True)
    time = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.id


class v_expense(models.Model):
    id = models.IntegerField(primary_key=True)
    e_no = models.IntegerField()
    v_name = models.CharField(max_length=50, null=True)
    v_number = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    amount = models.IntegerField()
    paid = models.IntegerField()
    due = models.IntegerField()
    date = models.CharField(max_length=50)
    product = models.CharField(max_length=50)
    p_quantity = models.IntegerField()

    def __str__(self):
        return self.id


class vendor_list(models.Model):
    id = models.IntegerField(primary_key=True)
    vendor_name = models.CharField(max_length=50, null=True)
    mobile_number = models.CharField(max_length=50, null=True)
    product_name = models.CharField(max_length=50, null=True)
    table_info = models.CharField(max_length=50, null=True)
    date = models.CharField(max_length=50, null=True)
    amount = models.FloatField(null=True)
    paid = models.FloatField(null=True)
    due = models.FloatField(null=True)
    status = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.id


class vendor_list_readyProduct(models.Model):
    id = models.IntegerField(primary_key=True)
    vendor_name = models.CharField(max_length=50, null=True)
    mobile_number = models.CharField(max_length=50, null=True)
    product_name = models.CharField(max_length=50, null=True)
    table_info = models.CharField(max_length=50, null=True)
    date = models.CharField(max_length=50, null=True)
    amount = models.FloatField(null=True)
    paid = models.FloatField(null=True)
    due = models.FloatField(null=True)
    status = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.id


class vendor_list_rowProduct(models.Model):
    id = models.IntegerField(primary_key=True)
    vendor_name = models.CharField(max_length=50, null=True)
    mobile_number = models.CharField(max_length=50, null=True)
    product_name = models.CharField(max_length=50, null=True)
    table_info = models.CharField(max_length=50, null=True)
    date = models.CharField(max_length=50, null=True)
    amount = models.FloatField(null=True)
    paid = models.FloatField(null=True)
    due = models.FloatField(null=True)
    status = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.id


class zzz_permanent_values(models.Model):
    id = models.IntegerField(primary_key=True)
    installed_date = models.CharField(max_length=50, null=True)
    currency = models.CharField(max_length=50, null=True)
    header = models.CharField(max_length=250, null=True)
    footer = models.CharField(max_length=250, null=True)
    tax = models.FloatField(max_length=50, null=True)
    theme_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.id


"""
CREATE TABLE [dbo].[zzz_permanent_values] (
    [Id]             INT           IDENTITY (1, 1) NOT NULL,
    [INSTALLED_DATE] VARCHAR (50)  NULL,
    [CURRENCY]       VARCHAR (50)  NULL,
    [HEADER]         VARCHAR (MAX) NULL,
    [FOOTER]         VARCHAR (MAX) NULL,
    [TAX]            FLOAT (53)    NULL,
    [THEME_NAME]     VARCHAR (50)  NULL,
    PRIMARY KEY CLUSTERED ([Id] ASC)
);
"""

"""
CREATE TABLE [dbo].[vendor_list_rowProduct] (
    [Id]            INT          IDENTITY (1, 1) NOT NULL,
    [vendor_name]   VARCHAR (50) NULL,
    [mobile_number] VARCHAR (50) NULL,
    [product_name]  VARCHAR (50) NULL,
    [table_info]    VARCHAR (50) NULL,
    [date]          VARCHAR (50) NULL,
    [amount]        FLOAT (53)   NULL,
    [paid]          FLOAT (53)   NULL,
    [due]           FLOAT (53)   NULL,
    [status]        VARCHAR (50) NULL,
    PRIMARY KEY CLUSTERED ([Id] ASC)
);
"""

"""
CREATE TABLE [dbo].[vendor_list_readyProduct] (
    [Id]            INT          IDENTITY (1, 1) NOT NULL,
    [vendor_name]   VARCHAR (50) NULL,
    [mobile_number] VARCHAR (50) NULL,
    [product_name]  VARCHAR (50) NULL,
    [table_info]    VARCHAR (50) NULL,
    [date]          VARCHAR (50) NULL,
    [amount]        FLOAT (53)   NULL,
    [paid]          FLOAT (53)   NULL,
    [due]           FLOAT (53)   NULL,
    [status]        VARCHAR (50) NULL,
    PRIMARY KEY CLUSTERED ([Id] ASC)
);
"""
"""
CREATE TABLE [dbo].[vendor_list] (
    [Id]            INT          IDENTITY (1, 1) NOT NULL,
    [vendor_name]   VARCHAR (50) NULL,
    [mobile_number] VARCHAR (50) NULL,
    [product_name]  VARCHAR (50) NULL,
    [table_info]    VARCHAR (50) NULL,
    [date]          VARCHAR (50) NULL,
    [amount]        FLOAT (53)   NULL,
    [paid]          FLOAT (53)   NULL,
    [due]           FLOAT (53)   NULL,
    [status]        VARCHAR (50) NULL,
    PRIMARY KEY CLUSTERED ([Id] ASC)
);

"""
"""
CREATE TABLE [dbo].[v_expense] (
    [Id]         INT          NOT NULL,
    [e_no]       INT          NOT NULL,
    [v_name]     VARCHAR (50) NULL,
    [v_number]   VARCHAR (50) NOT NULL,
    [status]     VARCHAR (50) NOT NULL,
    [amount]     INT          NOT NULL,
    [paid]       INT          NOT NULL,
    [due]        INT          NOT NULL,
    [date]       VARCHAR (50) NOT NULL,
    [product]    VARCHAR (50) NOT NULL,
    [p_quantity] INT          NOT NULL,
    PRIMARY KEY CLUSTERED ([Id] ASC)
);
"""

"""
CREATE TABLE [dbo].[userac] (
    [Id]       INT          NOT NULL,
    [Name]     VARCHAR (50) NOT NULL,
    [Email]    VARCHAR (50) NOT NULL,
    [Number]   VARCHAR (50) NOT NULL,
    [Password] VARCHAR (50) NOT NULL,
    [time]     VARCHAR (50) NOT NULL,
    PRIMARY KEY CLUSTERED ([Number] ASC)
);
"""

"""
CREATE TABLE [dbo].[trial_period_calculate] (
    [Id]                INT          NOT NULL,
    [trial_expire_date] VARCHAR (50) NULL,
    [expired]           VARCHAR (5)  NULL,
    [trial]             VARCHAR (50) NULL,
    PRIMARY KEY CLUSTERED ([Id] ASC)
);
"""
"""
CREATE TABLE [dbo].[theme_color] (
    [Id]                 INT          IDENTITY (1, 1) NOT NULL,
    [theme_name]         VARCHAR (50) NULL,
    [dv_bg_color]        VARCHAR (50) NULL,
    [dv_topbar_bg_color] VARCHAR (50) NULL,
    [dv_topbar_fg_color] VARCHAR (50) NULL,
    [pos_product_color]  VARCHAR (50) NULL,
    PRIMARY KEY CLUSTERED ([Id] ASC)
);
"""
"""
CREATE TABLE [dbo].[temp_sale_pos] (
    [Id]         INT          NOT NULL,
    [serial_no]  INT          NULL,
    [p_name]     VARCHAR (50) NULL,
    [qty]        INT          NULL,
    [taka]       FLOAT (53)   NULL,
    [p_code]     INT          NULL,
    [p_rate]     INT          NULL,
    [n_inStock]  INT          NULL,
    [p_barcode]  VARCHAR (50) NULL,
    [p_rate_buy] FLOAT (53)   NULL,
    PRIMARY KEY CLUSTERED ([Id] ASC)
);
"""
"""
CREATE TABLE [dbo].[temp_sale] (
    [Id]         INT          NOT NULL,
    [serial_no]  INT          NULL,
    [p_name]     VARCHAR (50) NULL,
    [qty]        INT          NULL,
    [taka]       FLOAT (53)   NULL,
    [p_code]     INT          NULL,
    [p_rate]     INT          NULL,
    [n_inStock]  INT          NULL,
    [p_barcode]  VARCHAR (50) NULL,
    [p_name_row] VARCHAR (50) NULL,
    [p_rate_buy] FLOAT (53)   NULL,
    PRIMARY KEY CLUSTERED ([Id] ASC)
);
"""

"""
CREATE TABLE [dbo].[temp_inventory_production_child_receipe] (
    [Id]           INT          NOT NULL,
    [p_name]       VARCHAR (50) NOT NULL,
    [p_code]       INT          NULL,
    [p_barcode]    VARCHAR (50) NULL,
    [quantity]     INT          NOT NULL,
    [cost]         FLOAT (53)   NOT NULL,
    [root_product] VARCHAR (50) NULL,
    PRIMARY KEY CLUSTERED ([Id] ASC)
);
"""
"""
CREATE TABLE [dbo].[sold_root_table_pos] (
    [Id]               INT           IDENTITY (1, 1) NOT NULL,
    [serial_no]        INT           NOT NULL,
    [time]             VARCHAR (50)  NULL,
    [date]             VARCHAR (50)  NULL,
    [total_products]   INT           NULL,
    [total_amount]     FLOAT (53)    NULL,
    [tax]              FLOAT (53)    NULL,
    [tax_amount]       FLOAT (53)    NULL,
    [with_tax]         FLOAT (53)    NULL,
    [customer_name]    VARCHAR (50)  NULL,
    [customer_number]  VARCHAR (50)  NULL,
    [customer_address] VARCHAR (MAX) NULL,
    [paid]             FLOAT (53)    NULL,
    [due]              FLOAT (53)    NULL,
    [status]           VARCHAR (50)  NULL,
    [company_name]     VARCHAR (50)  NULL,
    PRIMARY KEY CLUSTERED ([serial_no] ASC)
);
"""
"""
CREATE TABLE [dbo].[sold_root_table] (
    [Id]               INT           IDENTITY (1, 1) NOT NULL,
    [serial_no]        INT           NOT NULL,
    [time]             VARCHAR (50)  NULL,
    [date]             VARCHAR (50)  NULL,
    [total_products]   INT           NULL,
    [total_amount]     FLOAT (53)    NULL,
    [tax]              FLOAT (53)    NULL,
    [tax_amount]       FLOAT (53)    NULL,
    [with_tax]         FLOAT (53)    NULL,
    [customer_name]    VARCHAR (50)  NULL,
    [customer_number]  VARCHAR (50)  NULL,
    [customer_address] VARCHAR (MAX) NULL,
    [paid]             FLOAT (53)    NULL,
    [due]              FLOAT (53)    NULL,
    [status]           VARCHAR (50)  NULL,
    [company_name]     VARCHAR (50)  NULL,
    PRIMARY KEY CLUSTERED ([serial_no] ASC)
);
"""
"""
CREATE TABLE [dbo].[sold_child_table_pos] (
    [pk_no]      INT          IDENTITY (1, 1) NOT NULL,
    [Id]         INT          NOT NULL,
    [serial_no]  INT          NOT NULL,
    [p_name]     VARCHAR (50) NULL,
    [qty]        INT          NULL,
    [taka]       INT          NULL,
    [p_code]     INT          NULL,
    [p_rate]     INT          NULL,
    [n_instock]  INT          NULL,
    [p_barcode]  VARCHAR (50) NULL,
    [p_rate_buy] FLOAT (53)   NULL,
    PRIMARY KEY CLUSTERED ([pk_no] ASC),
    CONSTRAINT [FK_serial_no_pos] FOREIGN KEY ([serial_no]) REFERENCES [dbo].[sold_root_table_pos] ([serial_no])
);
"""


"""
CREATE TABLE [dbo].[sold_child_table] (
    [pk_no]      INT          IDENTITY (1, 1) NOT NULL,
    [Id]         INT          NOT NULL,
    [serial_no]  INT          NOT NULL,
    [p_name]     VARCHAR (50) NULL,
    [qty]        INT          NULL,
    [taka]       INT          NULL,
    [p_code]     INT          NULL,
    [p_rate]     INT          NULL,
    [n_instock]  INT          NULL,
    [p_barcode]  VARCHAR (50) NULL,
    [p_rate_buy] FLOAT (53)   NULL,
    PRIMARY KEY CLUSTERED ([pk_no] ASC),
    CONSTRAINT [FK_serial_no] FOREIGN KEY ([serial_no]) REFERENCES [dbo].[sold_root_table] ([serial_no])
);
"""

"""
CREATE TABLE [dbo].[serial_key] (
    [serial_no] INT NOT NULL,
    PRIMARY KEY CLUSTERED ([serial_no] ASC)
);
"""
"""
CREATE TABLE [dbo].[s_expense] (
    [Id]     INT          NOT NULL,
    [e_no]   INT          NOT NULL,
    [s_name] VARCHAR (50) NOT NULL,
    [status] VARCHAR (50) NOT NULL,
    [amount] INT          NOT NULL,
    [paid]   INT          NOT NULL,
    [due]    INT          NOT NULL,
    [date]   VARCHAR (50) NOT NULL,
    [reason] VARCHAR (50) NOT NULL,
    PRIMARY KEY CLUSTERED ([Id] ASC)
);
"""


"""
CREATE TABLE [dbo].[payments] (
    [Id]         INT          NOT NULL,
    [serial_no]  INT          NOT NULL,
    [reason]     VARCHAR (50) NOT NULL,
    [status]     VARCHAR (50) NOT NULL,
    [amount]     INT          NOT NULL,
    [paid]       INT          NOT NULL,
    [due]        INT          NOT NULL,
    [paid_date]  VARCHAR (50) NOT NULL,
    [paid_by]    VARCHAR (50) NULL,
    [his_number] VARCHAR (50) NOT NULL,
    [bill_by]    VARCHAR (50) NULL,
    PRIMARY KEY CLUSTERED ([serial_no] ASC)
);
"""

"""
CREATE TABLE [dbo].[m_expense] (
    [Id]       INT          NOT NULL,
    [e_no]     INT          NOT NULL,
    [e_reason] VARCHAR (50) NOT NULL,
    [status]   VARCHAR (50) NOT NULL,
    [amount]   INT          NOT NULL,
    [paid]     INT          NOT NULL,
    [due]      INT          NOT NULL,
    [date]     VARCHAR (50) NOT NULL,
    [e_by]     VARCHAR (50) NULL,
    [a_by]     VARCHAR (50) NULL,
    PRIMARY KEY CLUSTERED ([Id] ASC)
);
"""
"""
CREATE TABLE [dbo].[inventory_production_root_receipe] (
    [Id]              INT          IDENTITY (1, 1) NOT NULL,
    [p_name]          VARCHAR (50) NOT NULL,
    [p_code]          INT          NULL,
    [p_barcode]       VARCHAR (50) NULL,
    [net_amount]      INT          NULL,
    [net_amount_type] VARCHAR (10) NOT NULL,
    [product_cost]    FLOAT (53)   NOT NULL,
    [sell_ppu]        INT          NULL,
    PRIMARY KEY CLUSTERED ([Id] ASC)
);
"""

"""
CREATE TABLE [dbo].[inventory_production_child_receipe] (
    [Id]           INT          IDENTITY (1, 1) NOT NULL,
    [p_name]       VARCHAR (50) NOT NULL,
    [p_code]       INT          NULL,
    [p_barcode]    VARCHAR (50) NULL,
    [quantity]     INT          NOT NULL,
    [cost]         FLOAT (53)   NOT NULL,
    [root_product] VARCHAR (50) NULL,
    PRIMARY KEY CLUSTERED ([Id] ASC)
);
"""
"""
CREATE TABLE [dbo].[inventory_add_Rowstock] (
    [Id]                   INT          NOT NULL,
    [p_name]               VARCHAR (50) NOT NULL,
    [p_code]               INT          NULL,
    [p_barcode]            VARCHAR (50) NULL,
    [net_amount]           INT          NULL,
    [net_amount_type]      VARCHAR (10) NOT NULL,
    [category]             VARCHAR (20) NOT NULL,
    [in_stock]             INT          NOT NULL,
    [low_alert]            INT          NULL,
    [supply_ppu]           INT          NOT NULL,
    [sell_ppu]             INT          NULL,
    [discount]             INT          NOT NULL,
    [supplier]             VARCHAR (50) NULL,
    [tax]                  INT          NULL,
    [allow_change_on_edit] INT          NULL,
    [date]                 VARCHAR (50) NOT NULL,
    [mobile_number]        VARCHAR (50) NULL,
    PRIMARY KEY CLUSTERED ([Id] ASC)
);
"""
"""
CREATE TABLE [dbo].[inventory_add_Readystock] (
    [Id]                   INT          NOT NULL,
    [p_name]               VARCHAR (50) NOT NULL,
    [p_code]               INT          NULL,
    [p_barcode]            VARCHAR (50) NULL,
    [net_amount]           INT          NULL,
    [net_amount_type]      VARCHAR (10) NOT NULL,
    [category]             VARCHAR (20) NOT NULL,
    [in_stock]             INT          NOT NULL,
    [low_alert]            INT          NULL,
    [supply_ppu]           INT          NOT NULL,
    [sell_ppu]             INT          NULL,
    [discount]             INT          NOT NULL,
    [supplier]             VARCHAR (50) NULL,
    [tax]                  INT          NULL,
    [allow_change_on_edit] INT          NULL,
    [date]                 VARCHAR (50) NOT NULL,
    [mobile_number]        VARCHAR (50) NULL,
    PRIMARY KEY CLUSTERED ([Id] ASC)
);
"""
"""
CREATE TABLE [dbo].[customer_list] (
    [Id]               INT          IDENTITY (1, 1) NOT NULL,
    [customer_name]    VARCHAR (50) NULL,
    [mobile_number]    VARCHAR (50) NOT NULL,
    [company_name]     VARCHAR (50) NULL,
    [customer_address] VARCHAR (50) NULL,
    [serial_no]        INT          NOT NULL,
    [table_name]       VARCHAR (50) NULL,
    [status]           VARCHAR (50) NULL,
    [timedate]         VARCHAR (50) NULL,
    [amount]           FLOAT (53)   NULL,
    [paid]             FLOAT (53)   NULL,
    [due]              FLOAT (53)   NULL,
    PRIMARY KEY CLUSTERED ([Id] ASC)
);
"""
