---
title: Configuring IIS for SymProxy
description: Configuring IIS for SymProxy
ms.assetid: 66f1d05c-2572-4dda-a9d9-766561ebd491
keywords: ["SymProxy, IIS"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Configuring IIS for SymProxy


Internet Information Services (IIS) must be configured to use SymProxy as an Internet Server Application Programming Interface (ISAPI) filter. Furthermore, permissions must be set so that IIS can obtain symbols.

**To configure the application pool**

1.  From **Administrative Tools** open **Internet Information Services (IIS) Manager**.

2.  Expand the entry with the computer name on the left and locate **Application Pools**.

3.  Right-click **Application Pools** and choose **Add Application Pool**.

4.  For the **Name** type *SymProxy App Pool*.

5.  Under **.Net Framework version** select *None*

6.  Click **OK** to create the application pool.

7.  Next, right click the entry for the new application pool and select **Advanced Settings…**.

8.  Under **Process Model**, you will see **Identity**. Click the button at the right labeled "**…**".

    1.  If you are authenticating as a network service, select **Predefined** for the **Application Pool Identity** and then select **Network Service**.

    2.  If you are authenticating as a domain user, select **Custom account** and then click the **Set** button. Type the credentials of the account that has permissions to access the remote symbol server store (for example, *corp\\SymProxyUser*), and click **OK**.

9.  Click **OK** to exit the **Application Pool Identity** dialog.

10. Click **OK** to exit the **Advanced Settings** dialog.

**To set up the Virtual Directory**

1.  Expand **Web Sites**.

2.  Select **Default Web Site**.

3.  Right-click the **Symbols** virtual directory and choose **Properties**.

4.  In the **Virtual Directory** tab, click **Create**.

5.  From the **Application Pool** drop-down menu, choose **SymProxy App Pool**.

6.  To exit **Symbols Properties**, click **OK**.

**Configure the ISAPI Filter**

1.  Right-click the **Default Web Site** and select **Properties**.

2.  Double-click **ISAPI Filters**.

3.  Right click the center pane under the column **Name** and select Click **Add**.

4.  For **Filter Name** type **SymProxy** or some other meaningful name.

5.  For **Executable** type *c:\\windows\\system32\\inetsrv\\symproxy.dll*.

6.  To exit the **Filter Properties** dialog, click **OK**.

7.  To exit **Default Web Site Properties,** click **OK**.

 

 





