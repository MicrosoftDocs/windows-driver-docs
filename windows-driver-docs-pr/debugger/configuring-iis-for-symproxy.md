---
title: Configuring IIS for SymProxy
description: Configuring IIS for SymProxy
keywords: ["SymProxy, IIS"]
ms.date: 04/01/2021
ms.localizationpriority: medium
---

# Configuring IIS for SymProxy

Internet Information Services (IIS) must be configured to use SymProxy as an Internet Server Application Programming Interface (ISAPI) filter. Furthermore, permissions must be set so that IIS can obtain symbols.

For information on automating this process, and a summary of settings, see [SymProxy Automated Installation](symproxy-automated-installation.md).

Confirm that the example security settings are suitable for your environment and modify to adhere to any additional security requirements specific to your organization.

Configuration options will vary depending on the specific version of IIS you are running. For more information on IIS, refer to [IIS Web Server Overview](/iis/get-started/introduction-to-iis/iis-web-server-overview).

**To configure the application pool**

1.  Open **Internet Information Services (IIS) Manager**.

2.  Expand the entry with the computer name on the left and locate **Application Pools**.

3.  Right-click **Application Pools** and choose **Add Application Pool**.

4.  For the **Name** type *SymProxy App Pool*.

5.  Under **.Net CLR version** select *No Managed Code*

6.  Click **OK** to create the application pool.

7.  Next, right click the entry for the new application pool and select **Advanced Settings…**.

8.  Under **Process Model**, you will see **Identity**. Click the button at the right labeled "**…**".

    1.  If you are authenticating as a network service, select **Built-in account** for the **Application Pool Identity** and then select **Network Service**, and click **OK**.

    2.  If you are authenticating as a domain user, select **Custom account** and then click the **Set** button. Type the credentials of the account that has permissions to access the remote symbol server store (for example, *corp\\SymProxyUser*), and click **OK**.

9.  Click **OK** to exit the **Application Pool Identity** dialog.

10. Click **OK** to exit the **Advanced Settings** dialog.

**Example Virtual Directory Configuration**

1.  Expand **Sites**.

2.  Right-click the **Default Web Site** and select  **Add Virtual Directory**

3.  Use a name such as **Symbols** and map it to a selected location.

3.  Right-click the **Symbols** virtual directory that has been created and chose **Add Application**.

5.  From the **Application Pool** drop-down menu, choose **SymProxy App Pool** and click **OK**.

**Configure the ISAPI Filter**

1. Confirm that the ISAPI options are installed in IIS.

2.  Click on the **Default Web Site**.

3.  Double-click **ISAPI Filters**.

4.  Right click the center pane under the column **Name** and select Click **Add**.

5.  For **Filter Name** type **SymProxy** or some other meaningful name.

6.  For **Executable** type *c:\\windows\\system32\\inetsrv\\symproxy.dll*.

7.  To exit the **Filter Properties** dialog, click **OK**.

8.  To exit **Default Web Site Properties,** click **OK**.

**Configure MIME Types and Additional Configuration** 

The steps required are one part of the IIS symbol server and symproxy configuration. Refer to these topics for information on configuring MIME types and for information on other considerations.

[HTTP Symbol Stores](http-symbol-stores.md)

[Caching Acquired Symbol Files](caching-acquired-symbol-files.md)

[SymProxy Automated Installation](symproxy-automated-installation.md)
