---
title: Microsoft Bluetooth Test Platform
description: Bluetooth Test Platform (BTP) overview.
ms.assetid: a6beeecb-5967-4e08-bfe2-b8aae26861ad
ms.date: 4/17/2019
ms.localizationpriority: medium

---

# Tools in the BTP software package

The BTP software package contains several tools to be used for testing the Bluetooth.


## Download the BTP Software Package ##

## Version Updates ##



## Tools in the package ##

Follow the instructions to download TAEF from [**docs.microsoft.com**](https://docs.microsoft.com/en-us/windows-hardware/drivers/taef/getting-started)

To enable the use of the scripts for running tests, copy the TAEF binaries to:

- `c:\Taef`



### Known issues ###

- Power: If the device is plugged into a non-powered hub or VCC is not able to supply 5V intermittent failures may be seen. Please remedy by using a powered USB hub or use a 9V AC-DC Barrel adapter.

- Stress tests: If the test is run in a tight loop there an issue where the radios will not have finished disconnecting after the pairing test reports success before the next test attempts to pair resulting in a failure.