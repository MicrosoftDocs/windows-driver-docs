---
title: Programming Custom Credential Providers
description: Learn the process of implementing custom credential providers for Windows debuggers using DLLs, EXEs, or scripts for flexible authentication.
keywords: ["symbols, programming"]
ms.date: 11/20/2025
ms.topic: concept-article
---

# Program custom credential providers

Custom credential providers enable Windows debuggers to authenticate with symbol and source servers that use specialized authentication methods. This article shows you how to implement custom providers by using DLLs, executables, or scripts.

**What you learn:**

- Configure credential providers by using XML
- Implement providers as DLLs or executables
- Test and troubleshoot your custom provider

This article describes how to program a custom credential provider for the Windows debugger. With this provider, you can use additional symbol and source servers that require unique authentication types. The customization supports any type of authentication that the server requires. 

There are two options: 

- Custom provider implemented through an executable (or launched through CMD/BAT script).
- Custom provider implemented as a DLL by using the API interface described in this document.

## Windows debugger HTTPS authentication requests

The Windows debuggers request symbols from a symbol server. If the symbol server doesn't require authentication, the debuggers return the symbols without using any credential providers. If the symbol server returns a HTTP_STATUS_DENIED 401 (Unauthorized Access / Access Denied) status code, this status code indicates to the debugger that authentication is required. The 401 unauthorized code indicates that the request lacks valid authentication credentials for the target resource. This status code means the server refuses to fulfill the request because the client didn't provide the required authentication information. 

If you configure a custom credential provider, the debugger uses it and the credentials it returns to resend the failed request with the 401 error. The next section covers configuring a custom credential provider.

## XML configuration of the custom credential provider

To configure a custom credential provider, you need two XML files:

1. **DbgCredentialProvider.config.xml** - Specifies where configuration files are located
1. **Provider configuration XML** - Defines the provider implementation (DLL, EXE, or script)

When a 401 unauthorized error is returned, the debugger invokes DbgCredentialProvider.dll. This DLL looks for credential providers by following this process. It opens a file named DbgCredentialProvider.config.xml, which should be in the same directory as DbgCredentialProvider.dll. This file provides the folder location of the configuration XML files. 

### DbgCredentialProvider.config.xml search behavior

The search behavior used to locate the DbgCredentialProvider.config.xml file is described here. Once the process finds DbgCredentialProvider.config.xml, it opens the file and ends the search. The search runs in the following order:

1. It tries to locate the DbgCredentialProvider.config.xml file in the folder specified in the `DBG_COMMON_FOLDER` environment variable, if you set it.
1. It tries to locate the DbgCredentialProvider.config.xml file in the `%LOCALAPPDATA%\Dbg\Common` folder.
1. It tries to locate the DbgCredentialProvider.config.xml file in the folder of the calling application.
1. It tries to locate the DbgCredentialProvider.config.xml file in the folder next to DbgCredentialProvider.dll.

> [!NOTE]
> **DBG_COMMON_FOLDER** is an environment variable that specifies the folder location for debugger configuration files. When you set it, the debugger searches this location first for `DbgCredentialProvider.config.xml` before checking any default locations.

For information on how to set WinDbg-related environmental values, see [Environment Variables](environment-variables.md).

### XML configuration file location - DbgCredentialProvider.config.xml

The installation process places the config XML files at the folder locations specified in DbgCredentialProvider.config.xml.

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

You can list more than one folder under `<Folders></Folders>` elements. The folders can be a relative or absolute path. If you specify a relative path, it's relative to the location of the DbgCredentialProvider.config.xml file. The debugger searches the folders for providers in the order listed.

In the previous example, the `<Folders>` collection has just one folder, *CredentialProviders*, and it's a relative path.

### XML configuration information for the custom credential provider

After the debugger locates the specified folder location, it enumerates all files with the '*.xml*' extension in the *CredentialProviders* folder. The XML files describe which debugger credential providers are available for the debugger. The XML files describe the location of the credential providers (implemented in DLL, EXE, or CMD/BAT scripts). The providers' locations can be relative or absolute paths.

The debugger supports multiple custom credential providers. It asks every provider for credentials and uses the credentials from the first provider that returns success.

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

This example XML shows how to configure a DLL to be used as a credential provider.

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

In this example, there's just one provider - DbgCredentialProvider_gcmw.dll - which is located in the *GCMW* folder relative to the DbgCredentialProvider_gcmw.xml file location.

### Multiple credential providers

This example shows multiple credential providers. The providers are used, in the order listed, to get credentials for the requested host. As soon as one returns a valid token, that token is returned to the debugger and the following ones aren't used.

```xml
    <CredentialProviders> 

        <CredentialProvider ApiVersion="2.0.0" >GCMW\DbgCredentialProvider_gcmw.dll</CredentialProvider> 

        <CredentialProvider ApiVersion="2.0.0">OAuth2CredentialProvider\OAuth2CredentialProvider.cmd</CredentialProvider> 

    </CredentialProviders> 
```

## Use the command line to invoke the custom credential provider

This section describes how to implement the custom credential provider as an EXE or a CMD/BAT file command script. 

If you implement the provider as an EXE or a CMD script, design it to process the following command line parameters (case insensitive). You can't combine these parameters.

- Get
- Erase
- Store

### Get command

Use the `Get` command to retrieve a credential. The provider receives the remaining data through the standard input stream.

The standard input stream passes the additional input data to the provider, followed by an empty line that marks the end of the input parameters.

The parameters aren't case sensitive, so you can use any combination of uppercase and lowercase letters.

The provider can return an error through `error=zzzzz`.

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
| Protocol  | LPCWSTR  | HTTP or HTTPS. To increase security, use HTTPS. |
| Host      | LPCWSTR  | The name of the host server, such as contoso.symbols.com |
| Path      | LPCWSTR  | The path to the symbols directory, for example `apis/symbol/symsrv`. The caller/debugger makes sure that `Path` never starts with a '/' character |
| ResourceKind | LPCWSTR  | It can be "symbols" or "sources". Additional resource kinds might be added in the future. The credential provider implementation uses this field to adjust the required permissions when acquiring credentials. It also can be used to cache credentials for future use. |
| Interactive | bool | *true* = It's okay to display UI, *false* = no UI. |
| IsRetry| bool | When *true*, the provider must skip reading the caches and get new credentials. |
| ParentHwnd | HWND | The parent HWND if an authentication UI is displayed, for example `0x%I64x`. The applications can use the DBG_CREDENTIAL_PROVIDER_PARENT_HWND environment variable or the imagehlp/dbghelp `SymSetParentWindow` method to set up the parent HWND. |

You build the full URI/URL by concatenating `<protocol>://<host>/<path>` using the listed parameters, for example: `https://contoso.symbols.com/apis/symbol/symsrv`. The request looks like this:

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

The credential provider can use this command to erase the credentials from its cache. The input parameters are the same as for the `Get` command.
There's no output return value needed. An error might be returned.

### Store

The credential provider uses this command to store the credentials into its cache. The input parameters are the same as for the `Get` command. There's no output return value needed. An error might be returned.

### Local token cache and isRetry

For the initial request to the provider, the debugger sends the parameter `isRetry=false`. Some providers might get the token from their local cache. Once the debugger resends the HTTP request with this token, the server might return the 401 response again. This response might be because the token expired. Then the debugger asks the credential provider for a new token and this time with the parameter `isRetry=true`. In such a case, the provider shouldn't use its cache, but retrieve a brand new token.

## Interactive setting - authentication UI

In some non-interactive environments, such as test labs, no user is available to interact with a UI. In such cases, set the `issilent` parameter to *true*.
The provider shouldn't display any authentication or other UI when this parameter is true.

The scripts in test labs or applications can use the following options to control the interactive flag:

- Use the `!sym prompts off` or `!sym quiet` commands. For more information, see [**!sym prompts**](../debuggercmds/-sym.md).
- Use the `sflags` command line parameter of WinDbg or cdb/kd (SYMOPT_NO_PROMPTS flag).
- Use the [IDebugSymbols::SetSymbolOptions method](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols-setsymboloptions) (SYMOPT_NO_PROMPTS flag described in [Symbol Options](symbol-options.md))
- Use the [SymSetOptions function](/windows/win32/api/dbghelp/nf-dbghelp-symsetoptions) of imagehlp/dbghelp with SYMOPT_NO_PROMPTS flag.

### Set up the silent (non-interactive) symbol server

Use the [SymbolServerSetOptions function](/previous-versions/ff797954(v=vs.85)) to set up the silent (non-interactive) symbol server. If you set `SSRVOPT_UNATTENDED` to TRUE, SymSrv doesn't display dialog boxes or pop-ups. If you set the value to FALSE, SymSrv displays these graphical features when making connections.

#### Manage UI Windows

Some credential providers display an authentication UI. If so, they should use the `ParentHwnd` parameter so this UI appears as a modal dialog to the main debugger window. Otherwise, the authentication UI might be hidden behind the main debugger window and the user might think that the debugger isn't responding.

A debugger client application similar to WinDbg can use the `DBG_CREDENTIAL_PROVIDER_PARENT_HWND` environment variable or imagehlp/dbghelp [SymSetParentWindow](/windows/win32/api/dbghelp/nf-dbghelp-symsetparentwindow) method to set up the parent HWND. You can also use the [IDebugAdvanced2::Request](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugadvanced2-request) message `DEBUG_REQUEST_SET_PARENT_HWND` with value of HWND cast to UINT32.

## Return value requirements

The EXE or CMD/BAT script must return the username and password through the output stream as follows:

```text
username=aaa
password=bbb - where the password can be a password or PAT
```

### CredentialKind

The authentication request returns *CredentialKind*. CredentialKind has two options.

- Basic Authentication: Defined in RFC 7617. The system transmits credentials as user ID and password pairs encoded with Base64.

```text
username=xxx
credentialkind=Basic
password=yyy --> This can be a password or a PAT token
```

- Bearer Authentication: Defined in RFC 6750. The system uses bearer tokens in HTTP requests to access OAuth 2.0 protected resources.

```text
username=xxx
credentialkind=Bearer
header=Bearer <TOKEN_GOES_HERE> ---> Usually OAuth2 tokens begin with "ey" and it is a very long string
```

### Example of a CMD file

The following example shows a CMD file that returns an HTTP authentication header:

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

If you write a custom provider located in a CMD or EXE file, you can test it by launching it from a console window. For example:

```console
DebuggerCredentialManager.exe Get
```

This command starts the application. The application prints some information and then waits for user input. An empty line indicates the end of the user input.

```console
[Information] [DebuggerCredentialProvider.102949]Microsoft Debugger Credential Manager version 2024.0409.02656.285 (Windows, .NET 6.0.29) 'get'
```

Here's an example of the information you enter in the console window input stream. You can enter it in any combination of uppercase and lowercase.

```console
protocol=https
host=contoso.symbols.com
path=apis/symbol/symsrv
resourceKind=symbols
isretry=false 
issilent=false
parenthwnd=593598
```

Then press the ENTER key twice to send a blank line and indicate the end of user input.

The provider responds through the standard output stream.

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

The debugger ignores any lines that don't match the pattern `key=value`. The key must be one of the following values: protocol, host, path, username, credentialkind, or header. 

The debugger ignores case in the key value pairs. It treats a blank line as the end of input.

### Provider diagnostic information 

Providers can print diagnostic information on the output stream. The debugger ignores this information and doesn't display it to the user. The examples of extra information shown here are for illustration purposes only. Other providers might print different diagnostic information or not print anything.

#### PowerShell example script returning a PAT token

Here's a PowerShell script example that returns a PAT token.

The file PatCredentialProvider.xml configures the PATCredentialProvider.bat as the CredentialProvider.

```xml
<?xml version="1.0" encoding="utf-8"?>
<CredentialProviders>
     <CredentialProvider ApiVersion="2.0.0">PATCredentialProvider\PATCredentialProvider.bat</CredentialProvider>
</CredentialProviders>
```

The file PATCredentialProvider.bat is located in the PATCredentialProvider folder and calls PATCredentialProvider.ps1.

```console
@echo off
<PATH_TO_POWERSHELL>\PowerShell.exe -NoProfile -executionpolicy Unrestricted -WindowStyle Hidden -File "%~dp0\PATCredentialProvider.ps1"
```

The PATCredentialProvider.ps1 file is also located in the PATCredentialProvider folder.

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

### Overview

The following description covers the public interface credential providers must use if they implement a custom credential provider in a DLL. If you implement the provider in a DLL, you must export the GetUserCredentials method. These methods are located in `namespace Debugger::CredentialProvider::Provider`.

The required *DbgCredentialProviderImpl.h* header file is published with the Windows SDK. For information on downloading the SDK, see [Windows SDK](https://developer.microsoft.com/windows/downloads/windows-sdk/) and [SDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

### Message handling

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

### Response types

```cpp
enum CredentialResponseResultKind
{
    Success = 0,
    NoProviders, // There are no installed providers or can't launch 3rd party provider
    ProviderNotApplicable, // the provider can't handle requests to the provided URL
    Error
};
```

### Request structure

A structure stores the `GetUserCredentialsRequest`. It uses the same parameters as described in the preceding table.


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

### Work with credentials

A `GetUserCredentials` function requests the credentials to send to the symbol server in the HTTP request for symbols.

```cpp
HRESULT WINAPI GetUserCredentials(
  _In_ GetUserCredentialsRequest const & request,
  _Inout_ GetUserCredentialsResponse * pResponse);
```

The caller (debugger) of this method provides the request and response parameters. The caller ensures that the `UserName`, `Password`, and `ErrorMessage` are `nullptr` upon method entry. 

The implementation fills `UserName`, `Password`, `ErrorMessage` (optionally), and `Result`.

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

## Next steps

Now that you understand custom credential providers, try these tasks:

- [Set up your first credential provider using the CMD file example](#example-of-a-cmd-file)
- [Test your provider using the DebuggerCredentialManager.exe](#testing-a-custom-provider)
- [Review the C++ API for DLL implementations](#c-api-for-credential-providers-implemented-as-a-dll)

**Related articles:**

- [Symbols and Symbol Files](symbols-and-symbol-files.md)
- [Environment Variables](environment-variables.md)
