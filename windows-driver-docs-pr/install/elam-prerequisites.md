---
title: ELAM Prerequisites
description: Early Launch Antimalware drivers must adhere to the following program requirements to be signed by WHQL and loaded by Windows.
ms.assetid: 48759EB3-F8F9-4881-BD30-6D1252F08DFE
---

# ELAM Prerequisites


Early Launch Antimalware drivers must adhere to the following program requirements to be signed by **WHQL** and loaded by Windows.

## Antimalware Vendor Participation Requirements


Microsoft requires that Early Launch Antimalware vendors be members of the Microsoft Virus Initiative (MVI). This membership ensures that the vendors are active antimalware community participants with a positive industry reputation. Please reach out to wscisv@microsoft.com if you have any questions about ELAM driver signing.

## Hardware Certification Kit Tests


Each driver must pass the following HCK tests, which are administered by the ISV:

PERFORMANCE TEST
-   CALLBACK LATENCY - Each early launch AM driver is required to return the driver verification callbacks from the kernel within .5ms. This time is measured from when the kernel issues the callback to the driver to the time the driver returns the callback.
-   MEMORY ALLOCATION - Each early launch AM driver is required to limit its footprint in memory to 128 KB, for both the driver image as well as its configuration (signature) data.
-   UNLOAD BLOCKING - Each early launch AM driver receives a synchronous callback after the last boot driver has been initialized, which indicates that the AM driver will be unloaded. The AM driver can use this as an indication that it needs to do “cleanup” and save any status information that can be used by the runtime AM driver. However, the early launch AM driver must return the callback for the driver to be unloaded and for boot to continue.

SIGNATURE DATA TEST - Each early launch AM driver must get its malware signature data from a single, well-known location and no other. This allows measurement and protection of that data by Windows. This test ensures that each AM driver only reads its configuration data from the registry hive that is created for that driver.
BACKUP DRIVER TEST - The early launch AM driver, upon installation, must also install a backup copy of the driver to the backup driver store. This requirement is to help with remediation in the case that the primary driver gets corrupted. This test ensures that for an installed early launch AM driver, there is a corresponding driver in the backup store.
## Signed Binaries


Each driver .sys file must be code signed by Microsoft, using a special certificate indicating that it is an Early Launch AM Driver.

## Driver Binaries


The AM driver must be a single binary (not import any other DLLs).

## Windows Hardware Quality Lab (WHQL) submission


-   The ISV submits the driver package, along with its HCK test results, to the **WHQL** Portal. A parameter of the submission is an indication that the driver is an early launch driver.
-   The **WHQL** process verifies that the vendor is permitted to submit early launch drivers, and it verifies that the driver has passed its HCK tests.
-   The **WHQL** process creates a code signing catalog for the driver package.
-   **WHQL** returns to the vendor the signed catalog as well as the driver’s binaries signed by a special code signing certificate.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20ELAM%20Prerequisites%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




