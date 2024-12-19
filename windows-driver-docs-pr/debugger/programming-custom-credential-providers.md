---
title: Programming custom credential providers
description: This topic describes how to program a custom credential provider for the Windows debugger. 
keywords: ["symbols, programming"]
ms.date: 12/12/2024
---

# Programming custom credential providers

This topic describes how to program a custom credential provider for the Windows debugger. This allows for the use of additional symbol and source servers that require unique authentication types. The customization allows any type of authentication to be used that the server may require. 

There are two options: 

- Custom provider implemented via an executable (or launched via CMD/BAT script).
- Custom provider implemented as a DLL using the API interface described in this document.

## Windows debugger HTTPS authentication requests

The Windows debuggers request symbols from a symbol server, and if the symbol server does not require authentication, the symbols are returned without the use of any credential providers. If the symbol server returns a HTTP_STATUS_DENIED 401 (Unauthorized Access / Access Denied) status code, this indicates to the debugger that authentication is required.  The 401 unauthorized code indicates that the request lacks valid authentication credentials for the target resource. This means the server is refusing to fulfill the request because the client has not provided the required authentication information. 

If a custom credential provider is configured, it will be used and the credentials it returns, will be used to resend the failed with 401 error request. Configuring a custom credential provider, is covered in the next section of this topic.

## XML configuration of the custom credential provider

Two XML files are used to configure the custom credential provider, one that indicates the configuration file location, and a second file that contains the configuration information for the custom credential provider.

When a 401 unauthorized is returned, the debugger invokes DbgCredentialProvider.dll. This DLL will look for credential providers using the following process. It opens a file DbgCredentialProvider.config.xml which should be located in the same directory as DbgCredentialProvider.dll that provides the folder location of the configuration XML files. 

Note that the search behavior that is used to locate DbgCredentialProvider.config.xml file may change in the future.

### XML configuration file location - DbgCredentialProvider.config.xml

The config XML files are installed at the folder locations as specified in DbgCredentialProvider.config.xml.

```xml
<?xml version="1.0" encoding="utf-8"?>
<!--
The config file is located next to the DbgCredentialProvider.dll.
-->
<Settings>
    <Folders>
        <!--
        This is a list of the folders which should be provided as an absolute file path or
        relative to the location of this config file.
        -->
        <Folder>CredentialProviders</Folder>
    </Folders>
</Settings>
```

You can list more than one folder under `<Folders></Folders>` elements. The folders can be relative or absolute path. If it is relative path, it is relative to the location of the DbgCredentialProvider.config.xml file. The folders will be searched for providers in the order listed.

In the current example shown above, the Folders collection has just one folder "CredentialProviders" and it is a relative path.

### XML configuration information for the custom credential provider

After the specified folder location is located, all files with extension '*.xml' in CredentialProviders folder will be enumerated. The XML files describe which debugger credential providers are available for the debugger. The credential providers (implemented in DLL, EXE or CMD/BAT scripts) location is described in the CredentialProviders XML file. The providers may be relative or absolute paths.

Multiple custom credential providers are supported. The debugger will ask every provider for credentials and it will use the credentials from the first provider which returns success.

The order in which the XML files are enumerated is unspecified. 

The example DbgCredentialProvider_gcmw.xml file shows how a batch file can be called.

```xml
<?xml version="1.0" encoding="utf-8"?>
<CredentialProviders>
    <!--
          This is a list of the provider modules which should be provided as an absolute file path or
          relative to the location of this config file.
          The provider is a DLL, EXE or CMD file.
    -->
    <CredentialProvider>PATCredentialProvider\PATCredentialProvider.bat</CredentialProvider>

</CredentialProviders>
```

This example XML shows how a dll can be called.

```xml
<?xml version="1.0" encoding="utf-8"?>
<CredentialProviders>
    <!--
      This is a list of the provider modules which should be provided as an absolute file path or
      relative to the location of this config file.
      The provider is a DLL, EXE or CMD file.
    -->
   <CredentialProvider>GCMW\DbgCredentialProvider_gcmw.dll</CredentialProvider>

</CredentialProviders>
```

In this example we have just one provider DbgCredentialProvider_gcmw.dll and it is located in GCMW folder relative to the  DbgCredentialProvider_gcmw.xml file location. 

## Use the command line to invoke the custom credential provider

This section describes how the custom credential provider may be implemented as an EXE (or launched via CMD/BAT file command script). 

If the provider is implemented in EXE or a CMD script it should be able to process the following command line parameters (case insensitive), which cannot be combined with each other.

- Get
- Erase
- Store

### Get Command

The **Get** command is used to retrieve a credential. The remaining data will be passed to the provider via the standard input stream.

The additional input data will be passed to the provider via the standard input stream, followed by an empty line to mark the end of the input parameters.

The parameters are not case sensitive, and any combination of upper and lower case can be used.

An error may be returned via `error=zzzzz`

```text
Protocol=http or https
Host=xxx 
Path=yyy
ResourceKind=symbols or sources
Interactive=0 or 1
IsRetry=0 or 1
ParentHwnd=HWND
<empty line to mark the end of the input parameters>
```

### Get parameters

| Field     | Type  |  Description   |
|-----------|-------|--------------|
| Protocol  | LPCWSTR  | HTTP or HTTPS. To increase security, HTTPS is strongly recommended. |
| Host      | LPCWSTR  | The name of the host server, such as contoso.symbols.com |
| Path      | LPCWSTR  | The path to the symbols directory, for example `apis/symbol/symsrv`. The caller/debugger will make sure Path never starts with '/' character |
| ResourceKind | LPCWSTR  | It can be "symbols" or "sources". Additional resource kinds may be added in the future. The credential provider implementation may use this to adjust the required permissions when acquiring credentials. It also may be used to cache credentials for future use. |
| Interactive | bool | true - It is OK to display UI, false - no UI. |
| IsRetry| bool | When true the provider must skip reading the caches and get new credentials |
| ParentHwnd | HWND | The parent HWND if an authentication UI is displayed, for example 0x%I64x. The applications can use DBG_CREDENTIAL_PROVIDER_PARENT_HWND environment variable or imagehlp/dbghelp SymSetParentWindow method to setup the parent HWND. |

The full URI/URL is built by concatenating `<protocol>://<host>/<path>` using the listed parameters. For example: `https://contoso.symbols.com/apis/symbol/symsrv`. The request would look like this:

```console
protocol=https
host=contoso.symbols.com
path=apis/symbol/symsrv
resourceKind=symbols
isretry=false 
issilent=false
parenthwnd=593598
<Followed by an empty line to indicate the end of the input data.>
```

### Erase

The credential provider may choose to use this command to erase the credentials from its cache. The input parameters are same as for Get command.
There is no output return value needed. An Error may be returned.

### Store

The credential provider may choose to use this command to store the credentials into its cache. The input parameters are same as for Get command. There is no output return value needed. An Error may be returned.

### Local token cache and isRetry

For the very first request to the provider the debugger sends the parameter `isRetry=false`. Some providers may be getting the token from their local cache. Once the debugger resends the HTTP request with this token the server may return the 401 response again. This may be because the token has expired. Then the debugger will ask the credential provider for a new token and this time the isRetry=true. In such a case the provider should not use its cache, but retrieve a brand new token.

## Interactive setting - authentication UI

In some non-interactive environments, such as test labs, there may be no user to interact with a UI. In such a case the parameter issilent would be true.
The provider should not be displaying any authentication or other UI when this parameter is true.

The scripts in test labs or applications can use the following options to control the interactive flag.

- "!sym prompts off" or "!sym quiet" commands. For more information, see [**!sym prompts**](../debuggercmds/-sym.md).
- sflags command line parameter of WinDbg or cdb/kd (SYMOPT_NO_PROMPTS flag).
- [IDebugSymbols::SetSymbolOptions method](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols-setsymboloptions) (SYMOPT_NO_PROMPTS flag described in [Symbol Options](symbol-options.md))
- [SymSetOptions function](/windows/win32/api/dbghelp/nf-dbghelp-symsetoptions) of imagehlp/dbghelp with SYMOPT_NO_PROMPTS flag.

#### Setup the silent (non interactive) symbol sever

Use [SymbolServerSetOptions function](/previous-versions/ff797954(v=vs.85)) to setup the silent (non interactive) symbol sever. If `SSRVOPT_UNATTENDED` is set to TRUE, SymSrv will not display dialog boxes or pop-ups. If data is FALSE, SymSrv will display these graphical features when making connections.

#### Managing UI Windows

Some credential providers may display an authentication UI. If so, it should use the 'ParentHwnd' parameter so this UI would appear as a modal dialog to the main debugger window. Otherwise, the authentication UI may be hidden behind the main debugger window and the user may be given the impression that the debugger is "frozen".

A debugger client application similar to WinDbg may use DBG_CREDENTIAL_PROVIDER_PARENT_HWND environment variable or imagehlp/dbghelp [SymSetParentWindow](/windows/win32/api/dbghelp/nf-dbghelp-symsetparentwindow) method to setup the parent HWND. You can also use the [IDebugAdvanced2::Request](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugadvanced2-request) message `DEBUG_REQUEST_SET_PARENT_HWND` with value of HWND cast to UINT32.

## Return value requirements

The EXE or CMD/BAT script must return the username and password via the output stream as follows:

```text
username=aaa
password=bbb - where the password can be a password or PAT
```

### CredentialKind

The authentication request returns *CredentialKind*. There are two options for CredentialKind.

- Basic Authentication: Defined in RFC 7617. Credentials are transmitted as user-id/password pairs encoded using Base64.

```text
username=xxx
credentialkind=Basic
password=yyy --> This can be a password or a PAT token
```

- Bearer Authentication: Defined in RFC 6750. Bearer tokens are used in HTTP requests to access OAuth 2.0 protected resources.

```text
username=xxx
credentialkind=Bearer
header=Bearer <TOKEN_GOES_HERE> ---> Usually OAuth2 tokens begin with "ey" and it is a very long string
```

### Example CMD file

Here is an example of a CMD file which returns an HTTP authentication header:

OAuth2CredentialProvider.xml file located in CredentialProviders folder:

```xml
<?xml version="1.0" encoding="utf-8"?>
<CredentialProviders>
    <CredentialProvider ApiVersion="2.0.0" >OAuth2CredentialProvider\OAuth2CredentialProvider.cmd</CredentialProvider>
</CredentialProviders>	
```

OAuth2CredentialProvider.cmd file located in OAuth2CredentialProvider folder:

```cmd
@echo off
echo username=UserName@domain.com
echo header=Bearer <TOKEN_GOES_HERE>
```


## Testing a custom provider

If you are writing a custom provider located in a CMD or EXE file, you can test it simply by launching it from a console window using the commands. For example:

```console
DebuggerCredentialManager.exe Get
```

This would start the application, and print something like this and then will wait for user input (an empty line indicates end of the user input).

```console
[Information] [DebuggerCredentialProvider.102949]Microsoft Debugger Credential Manager version 2024.0409.02656.285 (Windows, .NET 6.0.29) 'get'
```

Here is an example of the information you enter in the console window input stream. It can be entered in any combination of upper and lower case.

```console
protocol=https
host=contoso.symbols.com
path=apis/symbol/symsrv
resourceKind=symbols
isretry=false 
issilent=false
parenthwnd=593598
```

Then press ENTER key twice to send a blank line and indicate the end of user input.

The provider responds via the standard output stream.

```console
[Verbose] [DebuggerCredentialProvider.103258]AzureCredentialProvider - Attempting to acquire bearer token using provider 'Msal Cache'
[Verbose] [DebuggerCredentialProvider.103300]Token expiration data - current UTC time:9/18/2024 5:33:00 PM, ExpiresOn: 9/18/2024 6:43:25 PM
[Information] [DebuggerCredentialProvider.103300]AzureCredentialProvider - Acquired bearer token using 'Msal Cache'
protocol=https
host=contoso.symbols.com
path=apis/symbol/symsrv
username=UserName@domain.com
credentialkind=Bearer
header=Bearer eyJ0eXAi....
<empty line>
```
The debugger will ignore any lines not matching the pattern `key=value` where key is one of the following: protocol, host, path, username, credentialkind, or header. 

Case is ignored in the key value pairs. The debugger treats a blank line as the end of input.

### Provider diagnostic information 

Providers may choose to print diagnostic information on the output stream. The debugger would ignore it, nor it will display those to the user. The examples of extra information shown here are for illustration purposes only. Other providers may print other diagnostic information or not print anything.

#### PowerShell example script returning a PAT token

Here is a PS script example of returning a PAT token.

The file PatCredentialProvider.xml configures the PATCredentialProvider.bat as the CredentialProvider.

```xml
<?xml version="1.0" encoding="utf-8"?>
<CredentialProviders>
     <CredentialProvider ApiVersion="2.0.0">PATCredentialProvider\PATCredentialProvider.bat</CredentialProvider>
</CredentialProviders>
```

The File PATCredentialProvider.bat located in PATCredentialProvider folder and calls PATCredentialProvider.ps1.

```console
@echo off
<PATH_TO_POWERSHELL>\PowerShell.exe -NoProfile -executionpolicy Unrestricted -WindowStyle Hidden -File "%~dp0\PATCredentialProvider.ps1"
```

The PATCredentialProvider.ps1 is also located in PATCredentialProvider folder.

```ps
<#
 .SYNOPSIS
    Given input, parses to find out which symbol server we want credentials for, and searches the Microsoft Credential Manager for those credentials.
    If found, prints the credentials to standard output. If not, prints error.

 .INPUT
    Delivered through standard input:
    protocol=http or https
    host=xxx ex. host=contoso.symbols.com
    path=yyy ex. path=apis/symbol/symsrv
    resourceKind=symbols
    isretry=false 
    issilent=false
    parenthwnd=593598
    <empty line to mark the end of the input parameters>

 .OUTPUT

    Delivered through standard output:

    username=aaa
    password=bbb - where the password can be a password or PAT. When PAT is returned the username will be any name (not necessarily the name of the currently logged in user)<!--[SuppressMessage("Microsoft.Security", "CS001:SecretInline", Justification="It's an example")]-->
    <empty line to mark the end of the output parameters>

 #>

 $logDirectory = (Get-Item Env:LoggingDirectory).Value
 $logFile = Join-Path $logDirectory "credProviderLog.txt"

 try
 {
    "Entering Credential Provider" | Out-File $logFile -Append

    $lines = While($line=Read-Host) {$line}
    $lines | Out-File $logFile -Append
    if (!(Get-Module "CredentialManager"))
    {
        "Installing module" | Out-File $logFile -Append

        Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201 -Force

        Install-Module CredentialManager -force -Scope CurrentUser
    }

    $pathLine = $lines | Where-Object {$_.StartsWith("path=")} | Select-Object -First 1
    "Found path line: $pathLine" | Out-File $logFile -Append

    [regex]$regex="path=(?<ServerName>.*)"
    $pathLine -Match $regex

    $symbolPath = "symbol:$($Matches.ServerName)"

    "Found symbol path: $symbolPath" | Out-File $logFile -Append

    $PAT = Get-StoredCredential -Target $symbolPath -AsCredentialObject

    if ($PAT)
    {
        "Found PAT!" | Out-File $logFile -Append
        Write-Host "username=placeholder"
        Write-Host "password=$($PAT.Password)"; # For OAuth 2 tokens You can change to output header=Bearer TOKEN
        Write-Host
    }
    else
    {
        "Could not locate PAT for Symbol Server: $symbolPath" | Out-File $logFile -Append
        Write-Host "error=Could not locate PAT for Symbol Server: $symbolPath"
    }
 }
 catch [System.SystemException]
 {
    "ERROR" | Out-File $logFile -Append
 
    $_ | Out-File $logFile -Append
 }
```
## C++ API for credential providers implemented as a DLL

The following describes the public interface credential providers must adhere to if the custom credential provider is implemented in a DLL. If the provider is implemented in a DLL it must export GetUserCredentials method. The are located in `namespace Debugger::CredentialProvider::Provider`.

The required *DbgCredentialProviderImpl.h* header file is published with the Windows SDK. For information on downloading the SDK, see [Windows SDK](https://developer.microsoft.com/windows/downloads/windows-sdk/) and [SDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

### MessageErrorLevelKind enums

```cpp
// The caller of this method should not terminate the message with '\r' or '\n' characters
// (which makes this method similar to PrintLine)
typedef void (*DbgPrintMessageFn)(_In_ MessageErrorLevelKind errorLevel, _In_ PCWSTR message);

enum class MessageErrorLevelKind : uint8_t
{
    Info = 0,
    Warning,
    Error
};
```

### CredentialResponseResultKind

```cpp
enum CredentialResponseResultKind
{
    Success = 0,
    NoProviders, // There are no installed providers or can't launch 3rd party provider
    ProviderNotApplicable, // the provider can't handle requests to the provided URL
    Error
};
```

### struct GetUserCredentialsRequest

A structure is used to store the GetUserCredentialsRequest. It uses the same parameters as described above in the GetUserCredentialsRequest parameters table.


```cpp
struct GetUserCredentialsRequest
{
    LPCWSTR Protocol;      // The full request URL can be built from Protocol, Host and Path as follows:
    LPCWSTR Host;          // Protocol://Host/Path
    LPCWSTR Path;          // The caller/debugger will make sure Path never starts with '/' character
    LPCWSTR ResourceKind;  // It can be "symbols", "sources", etc.
                           // The credential provider implementation may use this to adjust
                           // the required permissions when acquiring credentials. It also may be used
                           // to cache credentials for future use.
    bool Interactive;      // true - display UI is ok, false - no UI.
                           // Refer to the explanations above on how to setup a non interactive environment
    bool IsRetry;          // When true the provider may skip reading the caches and get new credentials
    HWND ParentHwnd;       // The parent HWND if an authentication UI is displayed.
                           // The applications can use DBG_CREDENTIAL_PROVIDER_PARENT_HWND environment variable
                           // or imagehlp/dbghelp SymSetParentWindow method to setup the parent HWND.

    DbgPrintMessageFn PrintMessageFn;
}
```

### GetUserCredentials function

A GetUserCredentials function is used to request the credentials, that will be sent to the symbol server in the HTTP request for symbols.

```cpp
HRESULT WINAPI GetUserCredentials(
  _In_ GetUserCredentialsRequest const & request,
  _Inout_ GetUserCredentialsResponse * pResponse);
```

The caller (debugger) of this method will provide the request and response parameters. The caller will ensure that the UserName, Password and ErrorMessage are nullptr upon method entry. 

The implementation should fill UserName, Password, ErrorMessage (optionally), and Result.

### GetUserCredentialsResponse class 

The GetUserCredentialsResponse class is shown here.

```cpp

class GetUserCredentialsResponse final
{
public:

    CredentialResponseResultKind Result = CredentialResponseResultKind::Error;
    BSTR UserName = nullptr;
    BSTR Password = nullptr;
    BSTR HttpAuthenticationHeader = nullptr;
    BSTR ErrorMessage = nullptr;

    GetUserCredentialsResponse() = default;

    GetUserCredentialsResponse(GetUserCredentialsResponse const&) = delete;
    GetUserCredentialsResponse& operator=(GetUserCredentialsResponse const&) = delete;

    GetUserCredentialsResponse(GetUserCredentialsResponse&& other) noexcept
    {
        Result = other.Result;
        UserName = other.UserName;
        Password = other.Password;
        HttpAuthenticationHeader = other.HttpAuthenticationHeader;
        ErrorMessage = other.ErrorMessage;

        other.Release();
    }

    GetUserCredentialsResponse& operator=(GetUserCredentialsResponse&& other) noexcept
    {
        if (this != addressof(other))
        {
            Clear();

            Result = other.Result;
            UserName = other.UserName;
            Password = other.Password;
            HttpAuthenticationHeader = other.HttpAuthenticationHeader;
            ErrorMessage = other.ErrorMessage;

            other.Release();
        }
        return (*this);
    }

    ~GetUserCredentialsResponse()
    {
        Clear();
    }

    void Clear()
    {
        SecureSysFreeString(UserName);
        SecureSysFreeString(Password);
        SecureSysFreeString(HttpAuthenticationHeader);
        SecureSysFreeString(ErrorMessage);
    }

private:
    template <class _Tp>
    _Tp* addressof(_Tp& __x) noexcept
    {
        return reinterpret_cast<_Tp*>(
            const_cast<char*>(&reinterpret_cast<const volatile char&>(__x)));
    }

    void Release() noexcept
    {
        Result = CredentialResponseResultKind::Error;
        UserName = nullptr;
        Password = nullptr;
        ErrorMessage = nullptr;
        HttpAuthenticationHeader = nullptr;
    }

    void SecureSysFreeString(_Inout_ BSTR& bstrString)
    {
        if (bstrString != nullptr)
        {
            size_t const length = wcslen(bstrString);
            SecureZeroMemory(bstrString, length * sizeof(wchar_t));
            SysFreeString(bstrString);
            bstrString = nullptr;
        }
    }
};
```

## See also

[Symbols and Symbol Files](symbols-and-symbol-files.md)

[Public and Private Symbols](public-and-private-symbols.md)
