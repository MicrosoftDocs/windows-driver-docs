---
title: How to Manage the PFA Memory List
description: How to Manage the PFA Memory List
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to Manage the PFA Memory List

Starting in Windows version 19042 bad memory pages are stored in the registry under "HKLM\SYSTEM\CurrentControlSet\Control\WHEA\BadPages". The reg command can be used to view the contents of this registry entry. Windows still respects any pages in the BCD system store, but all new pages will be stored in the registry.

1.  Click **Start**, point to **All Programs**, and then click **Accessories**.

2.  Right-click **Command Prompt** and select **Run as administrator**.

3.  If the User Account Control dialog box is displayed, click **Yes** in the dialog box.

### Viewing the current list of PFNs

To view the current list of PFNs in the system registry, run the following command:

``` syntax
reg query "HKLM\SYSTEM\CurrentControlSet\Control\WHEA" /v BadPages
```

If no ECC memory pages are predicted to fail, the output from the reg command appears as in the following example:

``` syntax
C:\Windows\system3>reg query "HKLM\SYSTEM\CurrentControlSet\Control\WHEA" /v BadPages


ERROR: The system was unable to find the specified registry key or value.
```

If ECC memory pages are predicted to fail, the BadPages regsitry key will contain a binary blob that contains all the pages, as shown in the following example:

``` syntax
C:\Windows\system32>reg query "HKLM\SYSTEM\CurrentControlSet\Control\WHEA" /v BadPages

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WHEA
    BadPages    REG_BINARY    000000000000000058140280000000005C1B0280000000007C30038000000000E2BBFC8000000000AF52188000F00F00
```

Powershell can be used to parse the registry data and ouput a list using the following script:

```
$whea = Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\WHEA"
$pages = $whea.BadPages
$idx = 0
while($idx -le $pages.Count) {
    $slice = $pages[$idx..($idx+7)]
    [array]::Reverse($slice)
    $page = (($slice | foreach { $_.ToString("X2") }) -join "")
    Write-Output $page
    $idx = $idx + 8
}

```

### Clearing the current list of PFNs

To clear the list of PFNs in the BCD system store, run the following command:

``` syntax
reg delete "HKLM\SYSTEM\CurrentControlSet\Control\WHEA" /v BadPages
```

**Note**  Improper changes to the registry can prevent Windows from starting. Therefore, you must review the commands and their results carefully before you restart Windows.

# How to Manage the PFA Memory List Prior To 19042

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

 

 

 




