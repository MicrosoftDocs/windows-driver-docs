---
title: How to Manage the PFA Memory List
description: How to Manage the PFA Memory List
ms.assetid: 28463f91-275b-4ad4-af64-59bed7fd3806
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 

 




