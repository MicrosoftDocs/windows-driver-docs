---
title: Setting Up the Web Site
description: Setting Up the Web Site
ms.assetid: 9c719557-bca0-4c9c-9208-70e106d976f9
---

# Setting Up the Web Site


Set up a Web site from which to share the source files and note the root directory of the site. Your source is then available from a site such as:

```
https://SrcMachineName/source
```

In order to make your source files accessible over the Internet, you must configure the directories containing the source files.

Begin by selecting the directory in which your indexed source resides. In our examples, we call this directory c:\\source and the name of the server on the network \\SrcMachineName. Permissions must be set so that users can access the site, and you must add the security groups that must access the source content over the network. The amount of security to enable varies from environment to environment. For some installations, this group is **Everyone**.

**To set up the permissions for the directory:**

1.  Open **Windows Explorer**.

2.  Expand **My Computer**.

3.  Expand the C: drive.

4.  Right-click **c:\\source** and choose **Sharing and Security**.

5.  Check the **Share this folder** button.

6.  Click the **Permissions** button.

7.  Verify that the desired security groups have read access by adding them under **Group or user names** and checking the appropriate box.

8.  Click **OK** to exit Permissions.

9.  Click **OK** to exit Source Properties.

The source directory can now be used for debugging by another computer with a source path of srv\*\\\\SrcMachineName\\source.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Setting%20Up%20the%20Web%20Site%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




