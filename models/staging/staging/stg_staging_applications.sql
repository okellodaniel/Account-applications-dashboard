{{ config(materialized="view") }}

with
    applications as (
        select *, row_number() over (partition by id, application_date) as rn
        from {{ source("staging", "applications_partitioned_clustered") }}
        where id is not null
    )
select
    -- identifiers
    {{ dbt_utils.generate_surrogate_key(["id", "application_date"]) }}
    as application_id,
    -- account details
    surname,
    given_name,
    account_name,
    account_type,
    alternative_account_type,
    alternative_bank_name,
    {{
        dbt.safe_cast(
            "alternative_mobile_money_number", api.Column.translate_type("integer")
        )
    }} as alternative_mobile_money_number,
    {{
        dbt.safe_cast(
            "alternative_phone_number", api.Column.translate_type("integer")
        )
    }} as alternative_phone_number,
    {{ dbt.safe_cast("tin", api.Column.translate_type("integer")) }} as tin,
    {{ dbt.safe_cast("card_number", api.Column.translate_type("integer")) }}
    as card_number,
    {{
        dbt.safe_cast(
            "alternative_bank_account_number", api.Column.translate_type("integer")
        )
    }} as alternative_bank_account_number,
      {{
        dbt.safe_cast(
            "phone_number", api.Column.translate_type("integer")
        )
    }} as phone_number,
    -- timestamps
    cast(application_date as timestamp) as application_date,
    cast(date_of_birth as timestamp) as date_of_birth,
    cast(expiry_date as timestamp) as expiry_date,
    cast(issue_date as timestamp) as issue_date,
    cast(application_submitted_at as timestamp) as application_submitted_at,
    cast(approval_request_date as timestamp) as approval_request_date,
    cast(approval_date as timestamp) as approval_date,
    cast(decline_date as timestamp) as decline_date,
    channel,
    currency,
    district,
    gender,
    monthly_income,
    marital_status,    
    nin,
    occupation,
    status,
    agent_code,   
    village,
    nationality,
    tenant_id
from applications
where rn = 1

-- -- dbt build --select <model_name> --vars '{'is_test_run': 'false'}'
-- {% if var("is_test_run", default=true) %} limit 100 {% endif %}
