---
title: Offline Symbols for Windows Update
description: This topic describes how you can work with off line symbols for Windows Update.
keywords: ["symbols", "setup, symbols", "symbols, setup"]
ms.author: domars
ms.date: 10/12/2018
ms.localizationpriority: medium
---

# Offline Symbols for Windows Update

This topic describes how you can work with offline symbols for Windows Update. It describes a procedure that can be used to decode Windows Update logs on machines that don’t have access to the Microsoft symbol server. 

If you find yourself needing to do this often, you should see if setting up a Symbol Proxy Server is viable for your networking configuration. For more information see [SymProxy](https://docs.microsoft.com/windows-hardware/drivers/debugger/symproxy).

All the options below require you to have one machine that can connect to Microsoft’s symbol server, and have the ability to copy files to or from the machine that has the logs. The machine that doesn’t have access to the symbol server will be referred to as the *offline* machine, and the machine that does have access as the *online* machine.

 We recommend using a single online machine per OS build version so the WU symbol cache will build month-by-month and contain the WU symbols from multiple update releases. 
 
If you have access to an online machine with the same exact patch level as the offline machine, you have two options:

•	[Option 1: Copy the ETL event log to the online machine](#ETL)

•	[Option 2: Copy the Symbols to offline machine](#OFFLINE)

Verify the online and offline PCs the same version level by running `winver` or `ver` on both machines.

```console
C:\>ver

Microsoft Windows [Version 10.0.17134.167]
```

If you don’t have access to an online machine with the same version, you’ll need to go through some extra steps to create a SymChk manifest file, described later in this topic in [Option 3: Create a SymChk manifest file](#SYMCHK).


## <span id="etl"></span><span id="ETL"></span>Option 1: Copy the ETL event log to the online machine

1. Copy all the WindowsUpdate ETL files from `C:\Windows\logs\WindowsUpdate\` to your online machine.

2. On the online machine, open a PowerShell prompt and run the following [Get-WindowsUpdateLog](https://docs.microsoft.com/powershell/module/windowsupdate/get-windowsupdatelog?view=win10-ps) PowerShell command. 

   ```powershell
   Get-WindowsUpdateLog -ETLPath <path to ETLs>
   ```
   This will download the symbols needed for log analysis.


## <span id="offline"></span><span id="OFFLINE"></span>Option 2: Copy the symbols to the offline machine

1. On the online machine, open a PowerShell prompt and run “Get-WindowsUpdateLog”. This will cache the symbols needed for log analysis.

2. Copy all the files in %temp%\WindowsUpdateLog\SymCache from the online machine to `%temp%\WindowsUpdateLog\SymCache` on the offline machine.

3. On the offline machine, open a PowerShell prompt and run “Get-WindowsUpdateLog” to analyze the logs.


## <span id="symchk"></span><span id="SYMCHK"></span>Option 3: Create a SymChk manifest file

1.	On the offline machine, follow steps at [Using a Manifest File with SymChk](https://docs.microsoft.com/windows-hardware/drivers/debugger/using-a-manifest-file-with-symchk) to create a manifest for these files in the system32 directory:

    ```console
    storewuauth.dll
    wuapi.dll
    wuauclt.exe
    wuaueng.dll
    wuautoappupdate.dll
    wuuhext.dll
    wuuhmobile.dll
    ```

2.	Copy the manifest to your online machine.

3.	With the manifest file, use SymChk to download the symbols locally to your online PC. 

4.	Copy the folder and symbols you passed to SymChk to %temp%\WindowsUpdateLog\SymCache on your offline PC.
 
5. On the offline machine, open a PowerShell prompt and run “Get-WindowsUpdateLog” to analyze the logs.

 



## See Also

[Using a Symbol Server](using-a-symbol-server.md).

[Symbol Path](symbol-path.md) 

[Accessing Symbols for Debugging](accessing-symbols-for-debugging.md)

[Symbol Problems While Debugging](symbol-problems-while-debugging.md)
 





