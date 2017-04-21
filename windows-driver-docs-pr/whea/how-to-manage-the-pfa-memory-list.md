---
title: How to Manage the PFA Memory List
author: windows-driver-content
description: How to Manage the PFA Memory List
ms.assetid: 28463f91-275b-4ad4-af64-59bed7fd3806
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# How to Manage the PFA Memory List


You can view and delete the list of memory pages that are saved in the BCD system store by using the BCDEdit command-line tool. To use the BCDEdit tool, you must be a member of the Administrators group on the computer and run BCDEdit from an elevated command prompt. To open an elevated command Prompt window, follow these steps:

1.  Click **Start**, point to **All Programs**, and then click **Accessories**.

2.  Right-click **Command Prompt** and select **Run as administrator**.

3.  If the User Account Control dialog box is displayed, click **Yes** in the dialog box.

### Viewing the current list of PFNs

To view the current list of PFNs in the BCD system store, run the following command:

``` syntax
C:\Windows\system32>bcdedit /enum {badmemory}
```

If no ECC memory pages are predicted to fail, the output from the BCDEdit tool appears as in the following example:

``` syntax
C:\Windows\system32>bcdedit /enum {badmemory}

RAM Defects
-----------
identifier              {badmemory}
```

If ECC memory pages are predicted to fail, the **{badmemory}** object contains a **badmemorylist** value. This value contains the list of PFNs for the memory pages that PFA predicts will fail, as shown in the following example:

``` syntax
C:\Windows\system32>bcdedit /enum {badmemory}

RAM Defects
-----------
identifier              {badmemory}
badmemorylist           0xffe38
                        0x100f
```

### Clearing the current list of PFNs

To clear the list of PFNs in the BCD system store, run the following command:

``` syntax
C:\Windows\system32>bcdedit /deletevalue {badmemory} badmemorylist
```

**Note**  Improper changes to the BCD system store can prevent Windows from starting. Therefore, you must review the commands and their results carefully before you restart Windows.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20How%20to%20Manage%20the%20PFA%20Memory%20List%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


