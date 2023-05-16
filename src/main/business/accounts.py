import time
import MergeAccountingClient
from MergeAccountingClient.api import accounts_api
from MergeAccountingClient.model.paginated_account_list import PaginatedAccountList
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
    api_instance = accounts_api.AccountsApi(api_client)
    cursor_next = cursor = "cj0xJnA9MjAyMy0wNS0xMiswMiUzQTQ1JTNBMDEuMTQ2ODU1JTJCMDAlM0EwMA==" # str | The pagination cursor value. (optional)
    x_account_token = "tFz5hvTIO9zAs-UGjPV8vqM4_O6sOA8EeNWcQte0JCr1tWzncDG3TA" # str | Token identifying the end user.
    all_data = []
    output =  open("file.txt", "w")
    while cursor_next:
        try:
            api_response = api_instance.accounts_list(x_account_token, cursor=cursor_next)
            print("Hello")
            all_data = all_data + api_response['results']
            cursor_next = api_response["previous"]
        except MergeAccountingClient.ApiException as e:
            print("Exception when calling AccountsApi->accounts_list: %s\n" % e)

        # example passing only required values which don't have defaults set
        # and optional values

    output.write(str(all_data))
