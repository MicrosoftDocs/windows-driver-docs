---
title: netsh mbn test installation
description: Netsh mbn test installation
ms.date: 03/01/2021
ms.localizationpriority: medium
---
# netsh mbn test
**netsh mbn test** is a test kit separate from the normal release version.
You need to install the Hardware Lab Kit (HLK) client first to enable this feature.

## HLK
Install the [HLK client](/windows-hardware/test/hlk/getstarted/step-2--install-client-on-the-test-system-s-) to enable the **netsh mbn test** function in DUT.

Alternatively, you can install [**HLK Taef Tool**](../taef/index.md) in the HLK package (path: installer\HLK-TAEF-TOOL-[arch-language]) to enable **netsh mbn test**.

Run the test command on the Device Under Test (DUT) that installed the HLK client.

Example:
```
netsh mbn test feature=connectivity param="AccessString=internet"
```

## VHLK

You can also use the [VHLK](/windows-hardware/test/hlk/getstarted/getstarted-vhlk) client to enable the **netsh mbn test** function in DUT.

Setup: Install VHLK on a host PC and run the script ConfigureTestSetup.ps1 <DUT's IP> from the location: C:\Program Files (x86)\Windows Kits\10\Hardware Lab Kit\Tests\amd64\Net\logo\Wwan

Then you can run the test command on the DUT. 

Example:

```
netsh mbn test feature=connectivity param="AccessString=internet"
```