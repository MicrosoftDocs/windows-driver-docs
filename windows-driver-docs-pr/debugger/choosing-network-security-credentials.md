---
title: Choosing Network Security Credentials
description: Choosing Network Security Credentials
ms.assetid: f53bda2b-a5e7-4a8e-ac31-44c92f306b7a
keywords: ["SymProxy, network security"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Choosing Network Security Credentials


The symbol proxy server must run from a security context with the appropriate privileges for access to the symbol stores that you plan to use. If you obtain symbols from an external Web store such as https://msdl.microsoft.com/download/symbols, the symbol proxy server must access the Web from outside of any firewalls. If you obtain files from other computers on your network, the symbol proxy server must have appropriate privileges to read files from those locations. Two possible choices are to set the symbol proxy server to authenticate as the **Network Service** account or to create a user account that is managed within Active Directory Domain Services along with other user accounts.

**Note**   It is a good practice to limit privileges of this account to only those necessary to read files and copy them to c:\\symstore. This restriction prevents clients that access your HTTP store from corrupting the system.

 

**Note**  Make sure the options presented here make sense in your environment. Different organizations have different security needs and requirements. Modify the process outlined here to support the security requirements of your organization.

 

### <span id="authenticate_as_a_network_service"></span><span id="AUTHENTICATE_AS_A_NETWORK_SERVICE"></span>Authenticate as a Network Service

The **Network Service** account is built in to Windows, so there is no extra step of creating a new account. For this example, we name the computer where the symbol proxy server is being configured *SymMachineName* on a domain named *corp*.

External symbol stores or Internet proxies must be configured to allow this computer's **Network Service** account (Machine Account) to authenticate successfully. There are two ways to achieve this:

-   Allow access to the **Authenticated Users** group on the external store or Internet proxy.

-   Allow access to the Machine Account *corp\\SymMachineName$*. This option is more secure because it limits access to just the symbol proxy server's "Network Service" account.

### <span id="Authenticate_as_a_Domain_User"></span><span id="authenticate_as_a_domain_user"></span><span id="AUTHENTICATE_AS_A_DOMAIN_USER"></span>Authenticate as a Domain User

For this example, we will presume the user account is named *SymProxyUser* on a domain called *corp*.

**To add the user account to the IIS\_USRS group**

1.  From **Administrative Tools** open **Computer Management**.

2.  Expand **Local Users and Groups**.

3.  Click **Groups**.

4.  Double-click **IIS\_USRS** in the center pane and select **Properties**.

5.  Under the **Members** section, click **Add**.

6.  Type *corp\\SymProxyUser* in the pane labeled **Enter the object name to select**.

7.  To exit the **Select Users, Computer, or Groups** dialog box, click **OK**.

8.  To exit **IIS\_USRS Properties**, click **OK**.

9.  Close the **Computer Management** console.

**Set up IIS to use the account**

1.  From **Administrative Tools** open **Internet Information Services (IIS) Manager**.

2.  Expand **Web Sites**.

3.  Right click **Default Web Site** and choose **Properties**.

4.  Click the **Directory Security** tab.

5.  In the **Authentication and access control** section, click **Edit…**.

6.  Make sure that *Enable anonymous access* is checked.

7.  Enter the credentials of the account that has permissions to access the remote symbol server store(s) (“corp\\SymProxyUser”) , then click **OK**.

8.  Re-enter the password when asked and click **OK**.

9.  To exit **Default Web Site Properties**, click **OK**.

10. You may be presented with the *Inheritance Overrides* dialog. If so, select which virtual directories you want to have this apply to.

### <span id="authenticate_as_a_domain_user"></span><span id="AUTHENTICATE_AS_A_DOMAIN_USER"></span>Authenticate as a Domain User Using the IIS\_WPG group

For this example, the user account is named *SymProxyUser* on a domain named *corp*. To authenticate this user account, it must be added to the **IIS\_WPG** group.

**To add the user account to the IIS\_WPG group**

1.  From **Administrative Tools** open **Computer Management**.

2.  Expand **Local Users and Groups**.

3.  Click **Groups**.

4.  Double-click **IIS\_WPG** in the right pane.

5.  Click **Add**.

6.  Type *corp\\SymProxyUser* in the pane labeled **Enter the object name to select**.

7.  To exit the **Select Users, Computer, or Groups** dialog box, click **OK**.

8.  To exit **IIS\_WPG Properties**, click **OK**.

9.  Close the **Computer Management** console.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Choosing%20Network%20Security%20Credentials%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




