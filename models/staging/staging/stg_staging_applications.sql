with 

source as (

    select * from {{ source('staging', 'applications') }}

),

renamed as (

    select
        id,
        tenant_id,
        application_date,
        account_name,
        account_type,
        alternative_account_type,
        alternative_mobile_money_number,
        alternative_phone_number,
        alternative_bank_name,
        tin,
        card_number,
        channel,
        currency,
        date_of_birth,
        district,
        expiry_date,
        gender,
        given_name,
        issue_date,
        marital_status,
        monthly_income,
        nin,
        occupation,
        phone_number,
        status,
        surname,
        village,
        nationality,
        agent_code,
        application_submitted_at,
        approval_request_date,
        approval_date,
        decline_date,
        alternative_bank_account_number

    from source

)

select * from renamed
