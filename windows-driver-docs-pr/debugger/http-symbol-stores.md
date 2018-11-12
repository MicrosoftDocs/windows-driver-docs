---
title: HTTP Symbol Stores
description: HTTP Symbol Stores
ms.assetid: b7dd1f3c-0135-4b69-9d70-b7cbf37fa969
keywords: ["HTTP symbol stores"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# HTTP Symbol Stores


## <span id="ddk_using_other_symbol_stores_dbg"></span><span id="DDK_USING_OTHER_SYMBOL_STORES_DBG"></span>


By using the SRV protocol supported through symsrv.dll (shipped with debugger), the symbol store can be accessed using HTTP (instead of just UNC/SMB).

HTTP is commonly used instead of SMB when a firewall doesn’t allow SMB between the client and the server. Production and Lab environments are good examples of this.

An HTTP symbol server can’t be a downstream store in a symbol path chain due to its read-only nature. Symbol Server Proxy (ISAPI Filter) works around this limit. SymProxy downloads the missing files to the server’s file system using preconfigured upstream symbol stores. The filter downloads the file to the file system, allowing IIS to download the file to the client, thereby restoring the concept of symbol store chaining. Refer to [SymProxy](symproxy.md) for more information.

Configuring IIS as a symbol store is relatively easy as the symbol files are just served as static files. The only non-default setting is the configuration of the MIME Types to allow the download of the symbol files as binary streams. This can be done by using a “\*” wildcard applied to the virtual directory of the symbol folder.

In order to make a symbol store accessible over the Internet, you must configure both the directories containing the symbol files and Internet Information Services (IIS).

**Note**  Because of the way IIS will be configured to serve symbol files, it is not recommended that the same server instance be used for any other purpose. Typically the desired security settings for a symbol server will not make sense for other uses, for example for an external facing commerce server. Make sure that the sample configuration described here makes sense for your environment and adapt it as appropriate for your specific needs.

 

### <span id="configuring_the_directories"></span><span id="CONFIGURING_THE_DIRECTORIES"></span>Creating the Symbol Directory

Begin by selecting the directory you will use as your symbol store. In our examples, we call this directory c:\\symstore and the name of the server on the network is \\SymMachineName.

For details on how to populate your symbol store, see [SymStore](symstore.md) and [Symbol Store Folder Tree](symbol-store-folder-tree.md).

### <span id="configuring_iis"></span><span id="CONFIGURING_IIS"></span>Configuring IIS

Internet Information Services (IIS) must be configured to serve the symbols by creating a virtual directory and configuring MIME types. After this has been done, the authentication method may be chosen.

**To create a virtual directory**

1.  From **Administrative Tools** open **Internet Information Services (IIS) Manager**.

2.  Navigate to **Web Sites**.

3.  Right-click **Default Web Site** or the name of the site being used and select **Add Virtual Directory…**.

4.  Type **Symbols** for **Alias** and click **Next**.

    For ease of administration, it’s recommended that the same name be used for the Folder, Share and Virtual Directory.

5.  For the **Path** enter **c:\\SymStore** and click **Next**.

6.  Click **OK** to finish the adding the virtual directory.

Perform the subdirectory configuration process once for the server. Note that this is a global setting and will effect applications not hosted in the root folder of a site.

**Subdirectory Configuration**

1.  Navigate to **\[Computer\]**.

2.  Open the **Configuration Editor**.

3.  Navigate to **system ApplicationHost/sites**.

4.  Expand **virtualDirectoryDefaults**.

5.  Set **allowSubDirConfig** to *False*.

Perform this process once for the server. Note that this is a global setting and will effect applications not hosted in the root folder of a site.

**Optionaly Make the Symbol Files Browseable**

1.  Navigate to **\[Computer\] | Sites | \[Web Site\] | Symbols**.

2.  Double click **Directory Browsing** in the center pane.

3.  Click **Enable** in the right pane.

The MIME Type for the downloaded content needs to be set to application/octet-stream to allow all symbols files to be delivered by IIS.

**Configuring MIME types**

1. Right-click the **Symbols** virtual directory and choose **Properties**.

2. Select **HTTP Headers**.

3. Click **MIME Types**.

4. Click **New**.

5. For **Extension**, type **\\***.

6. For **MIME type**, type **application/octet-stream**.

7. To exit the **MIME Types** dialog box, click **OK**.

8. To exit **Symbols Properties**, click **OK**.

You can edit the web.config file to configure MIME types for Symbols. This approach clears the inherited MIME Types and adds a catch-all wild card \* MIME Type. This approach may be necessary when MIME types are being inherited in certain IIS configurations.

**Using web.config to configure MIME types**

1.  Edit the web.config file as shown here.

    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <configuration>
        <system.webServer>
            <directoryBrowse enabled="true" />
            <staticContent>
                <clear />
                <mimeMap fileExtension=".*" 
    mimeType="application/octet-stream" />
            </staticContent>
        </system.webServer>
    </configuration>
    ```

2.  Restart IIS.

IIS is now ready to serve symbol files of all types from the symbol store.

## <span id="Configuring_Authentication"></span><span id="configuring_authentication"></span><span id="CONFIGURING_AUTHENTICATION"></span>Configuring Authentication


It is possible to configure IIS to use “Integrated Windows Authentication” so that clients (windbg.exe for example) can automatically authenticate against IIS without prompting the end-user for credentials.

**Note**  Only configure Windows Authentication on IIS to control access to the symbol server if that is appropriate for your environment. There are other security options available to further control access to IIS if that is required for your environment.

 

**To configure the authentication method as Anonymous**

1.  Launch the **Internet Information Services (IIS) Manager**.

2.  Navigate to **\[Computer\] | Sites | \[Web Site\] | Symbols**.

3.  Double click **Authentication** in the center pane.

4.  Under **Authentication and access control** click **Edit**.

5.  Right click **Windows Authentication** and select **Enable**.

6.  For all other authentication providers, right click each provider and select **Disable**.

7.  Click **OK** to finish configuring authentication.

If Window Authentication is not listed, use **Turn Windows features on and off** to enable the feature. The location of the feature is different in each version of Windows. In Windows 8.1/Windows 2012 R2, it is located under Internet Information Services | World Wide Web Services | Security.

## <span id="Disable_Kerberos_Support"></span><span id="disable_kerberos_support"></span><span id="DISABLE_KERBEROS_SUPPORT"></span>Disable Kerberos Support


SymSrv.dll does not support Kerberos authentication when connecting to IIS. As such, Kerberos authentication must be disabled in IIS and NTLM needs to be set as the only Windows Authentication protocol.

**Note**  Only disable Kerberos security if that is appropriate for your environment.

 

**Disable Kerberos Support Using appcmd.exe**

1.  Open a Command Prompt window

2.  To disable Kerberos and force the use of NTLM, use this command:

    ```console
    appcmd.exe set config -section:system.webServer/security/authentication/windowsAuthentication /+"providers.[value='NTLM']" /commit:apphost
    ```

3.  To return to the default value with Kerberos enabled, use this command:

    ```console
    appcmd.exe set config -section:system.webServer/security/authentication/windowsAuthentication /+"providers.[value='Negotiate,NTLM']" /commit:apphost
    ```

## <span id="Configuring_SymSrv_Client_Authentication_Prompts"></span><span id="configuring_symsrv_client_authentication_prompts"></span><span id="CONFIGURING_SYMSRV_CLIENT_AUTHENTICATION_PROMPTS"></span>Configuring SymSrv Client Authentication Prompts


When SymSrv receives authentication requests, the debugger can either display the authentication dialog box or automatically refuse the request, depending on how it has been configured. You can configure this behavior using !sym prompts on|off. For example to turn prompts on, use this command.

```dbgcmd
!sym prompts on
```

To check the current setting, use this command.

```dbgcmd
!sym prompts
```

For more information see [**!sym**](-sym.md) and [Firewalls and Proxy Servers](firewalls-and-proxy-servers.md).

 

 





