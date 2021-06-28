---
title: How to Manage the PFA Memory List
description: How to Manage the PFA Memory List
ms.date: 06/28/2021
ms.localizationpriority: medium
---

# How to Manage the Predictive Failure Analysis (PFA) Memory List



Whenever Predictive Failure Analysis (PFA) predicts that an Error Correction Code (ECC) memory page is likely to fail based on the current PFA registry settings,
PFA stores (or *persists*) the page frame number (PFN) for the memory page.


Starting in Windows version 19042, bad memory pages are stored in the registry under `HKLM\SYSTEM\CurrentControlSet\Control\WHEA\BadPages`.
In previous versions of Windows, this information is stored in the BCD system store.

This list contains the PFNs for all memory pages that the PFA has predicted are likely to fail.
When Windows starts, it excludes these memory pages from system use.

> [!NOTE]
> There is no industry standard for mapping a physical memory PFN to a specific physical memory module. Thus, WHEA cannot provide information about which memory modules are failing.

When the failing system memory is replaced, a system administrator must clear this list manually by updating the registry or using the BCDEdit command-line tool.
If the list is not cleared, Windows continues to exclude the memory pages in the list even if the failing memory modules have been replaced.

To perform the steps described on this page, you need to open an elevated command prompt:

1. Click **Start**, point to **All Programs**, and then click **Accessories**.
2. Right-click **Command Prompt** and select **Run as administrator**.
3. If the User Account Control dialog box is displayed, click **Yes** in the dialog box.

## Viewing Page Frame Numbers (PFNs) in the registry

To view the current list of PFNs in the system registry, run the following command from your elevated command prompt:

```cmd
reg query "HKLM\SYSTEM\CurrentControlSet\Control\WHEA" /v BadPages
```

If no ECC memory pages are predicted to fail, the output from the reg command appears as in the following example:

```console
C:\Windows\system32>reg query "HKLM\SYSTEM\CurrentControlSet\Control\WHEA" /v BadPages


ERROR: The system was unable to find the specified registry key or value.
```

If ECC memory pages are predicted to fail, the BadPages registry key contains a binary blob that encapsulates the pages, as shown in the following example:

```console
C:\Windows\system32>reg query "HKLM\SYSTEM\CurrentControlSet\Control\WHEA" /v BadPages

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WHEA
    BadPages    REG_BINARY    000000000000000058140280000000005C1B0280000000007C30038000000000E2BBFC8000000000AF52188000F00F00
```

You can use PowerShell to parse the registry data and ouput a list using the following script:

```powershell
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

## Clearing PFNs from the registry

To clear the list of PFNs in the BCD system store, use the following command:

```console
reg delete "HKLM\SYSTEM\CurrentControlSet\Control\WHEA" /v BadPages
```

**Note**  Improper changes to the registry can prevent Windows from starting. Therefore, you must review the commands and their results carefully before you restart Windows.

## Viewing the current list of PFNs in the BCD system store


You can view and delete the list of memory pages that are saved in the BCD system store by using the BCDEdit command-line tool.
See [BCDEdit Command-Line Options](/windows-hardware/manufacture/desktop/bcdedit-command-line-options) for the list of options you can use.

To use the BCDEdit tool, you must be a member of the Administrators group on the computer.

Use the following command from your elevated command prompt:

```console
C:\Windows\system32>bcdedit /enum {badmemory}
```

If no ECC memory pages are predicted to fail, the output from the BCDEdit tool appears as in the following example:

```console
C:\Windows\system32>bcdedit /enum {badmemory}

RAM Defects
-----------
identifier              {badmemory}
```

If ECC memory pages are predicted to fail, the **{badmemory}** object contains a **badmemorylist** value. This value contains the list of PFNs for the memory pages that PFA predicts will fail, as shown in the following example:

```console
C:\Windows\system32>bcdedit /enum {badmemory}

RAM Defects
-----------
identifier              {badmemory}
badmemorylist           0xffe38
                        0x100f
```

## Clearing the current list of PFNs from the BCD system store

To clear the list of PFNs in the BCD system store, run the following command:

``` syntax
C:\Windows\system32>bcdedit /deletevalue {badmemory} badmemorylist
```

> [!NOTE]
> Improper changes to the BCD system store can prevent Windows from starting. Therefore, you must review the commands and their results carefully before you restart Windows.

