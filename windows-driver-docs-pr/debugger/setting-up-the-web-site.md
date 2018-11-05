---
title: Setting Up the Web Site
description: Setting Up the Web Site
ms.assetid: 9c719557-bca0-4c9c-9208-70e106d976f9
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Setting Up the Web Site


Set up a Web site from which to share the source files and note the root directory of the site. Your source is then available from a site such as:

```text
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

 

 





