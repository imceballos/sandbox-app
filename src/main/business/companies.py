import time
import MergeAccountingClient
from MergeAccountingClient.api import company_info_api
from MergeAccountingClient.model.paginated_company_info_list import PaginatedCompanyInfoList
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/accounting/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergeAccountingClient.Configuration(
    host = "https://api.merge.dev/api/accounting/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'kVZXEiHb1eEsmJEuCXGXatSur9ip8Q_mSM_2P8_ddRZyL5zZg8CQkw'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with MergeAccountingClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = company_info_api.CompanyInfoApi(api_client) 
    x_account_token = "tFz5hvTIO9zAs-UGjPV8vqM4_O6sOA8EeNWcQte0JCr1tWzncDG3TA" # str | Token identifying the end user.
    #created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    #created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cj0xJnA9MjAyMS0wMS0wNiswMyUzQTI0JTNBNTMuNDM0MzI2JTJCMDAlM0EwMA==" # str | The pagination cursor value. (optional)
    expand = "addresses,phone_numbers" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_deleted_data = True # bool | Whether to include data that was marked as deleted by third party webhooks. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    #modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified after this datetime. (optional)
    #modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified before this datetime. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.company_info_list(x_account_token)
        pprint(api_response)
    except MergeAccountingClient.ApiException as e:
        print("Exception when calling CompanyInfoApi->company_info_list: %s\n" % e)