import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import transactions_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/accounting/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergePythonSDK.accounting.Configuration(
    host = "https://api.merge.dev/api/accounting/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: accountTokenAuth
configuration.api_key['accountTokenAuth'] = "tFz5hvTIO9zAs-UGjPV8vqM4_O6sOA8EeNWcQte0JCr1tWzncDG3TA"

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
configuration.api_key_prefix['accountTokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = MergePythonSDK.accounting.Configuration(
    access_token = 'kVZXEiHb1eEsmJEuCXGXatSur9ip8Q_mSM_2P8_ddRZyL5zZg8CQkw'
)

# Enter a context with an instance of the API client
with MergePythonSDK.accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    company_id = "company_id_example" # str | If provided, will only return accounting transactions for this company. (optional)
    #created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    #created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "line_items,tracking_categories,contact,account" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_deleted_data = True # bool | Whether to include data that was marked as deleted by third party webhooks. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    #modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge after this date time will be returned. (optional)
    #modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge before this date time will be returned. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)
    #transaction_date_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | If provided, will only return objects created after this datetime. (optional)
    #transaction_date_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | If provided, will only return objects created before this datetime. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    while cursor_next:
        try:
            api_response = api_instance.transactions_list(cursor=cursor)
            api_response
            print("Hello")
            cursor_next = api_response["next"]
        except MergePythonSDK.accounting.ApiException as e:
            print("Exception when calling TransactionsApi->transactions_list: %s\n" % e)