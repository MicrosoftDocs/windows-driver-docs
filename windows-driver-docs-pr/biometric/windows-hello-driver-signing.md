---
title: Windows Hello fingerprint driver signature process
description: Windows Hello fingerprint driver signature process
keywords:
- biometric drivers WDK , windows hello
- signing biometric drivers
ms.date: 03/03/2023
---


# Windows Hello: Steps to Submit a Fingerprint Driver


## Submitting a fingerprint driver for Windows Hello compatibility 
Microsoft has introduced new requirements on biometric sensors to comply with Windows Hello quality guidelines. A new manual review process will be necessary to gain approval to interoperate with Windows Hello. The process will be enforced with an OS check for a specific signature obtained through the Windows DevCenter (here: https://developer.microsoft.com/) that can only be obtained by undergoing the process in this document. Drivers that have been created and signed by WHQL before 6/1/17 are grandfathered. New and updated drivers that do not obtain this signature after this date will not work with Windows Hello in Window 10, version 1703 or later after the enforcement date.

A driver will always undergo manual approval to obtain the Windows Hello signature. Updates to approved drivers can refer to previous submissions for faster approval. Drivers must undergo a new review if it applies to a new sensor, or if changes to the matching engine have occurred that impact FAR, FRR, or presentation attack detection. 

The biometric signature enforcement date is 6/1/2017, after which drivers that do not contain the bio signature will not be loaded and will no longer work with Windows Hello.

### Step One: Create a biometric driver
Follow the instructions here to create a biometric driver: 

[Windows Biometric Framework](/windows/desktop/SecBioMet/biometric-service-api-portal)

### Step Two: Test your sensor and self-validate
Self validate the sensor and driver to ensure they meet Microsoft’s biometric requirements and report findings in the Fingerprint Security Review Template. Documents for the requirements and template can be found within the Fingerprint partner package on Connect. If you do not have access to Connect, contact your Microsoft representative.

### Step Three: Modify the driver configuration xml file
When you submit your driver, the Windows 10, version 1703 Fingerprint HLK test will check to ensure that the `<vendorCompliance>` and `<securityReview>` tag are included with the following fields:

**bugId**: ID number for the previous HLK submission that contains the previously approved security review information or 0 if the submission is undergoing an entirely new security review.

**updateExistingSubmission**: true if the submission serves as an update to a previous submission that has undergone the security review and false if otherwise.

#### Example
 ```cpp
<?xml version="1.0" encoding="utf-8"?>
<bioTestConfiguration version="0" runOptional="false" runInteractive="true" abortOnFailure="false" manualStep="false" priority="3" logType="WTT">
  <vendorCompliance>
    <securityReview bugId="12345678" updateExistingSubmission="true"/>
  </vendorCompliance>
  <testSuites>
    <testSuite deviceRequired="false" id="StorageAdapter">
      <library>storagetest.dll</library>
      <description>storage Adapter Test Suite</description>
    </testSuite>
  </testSuites>
  <deviceInfo>
         <sensorAdapterLib>WinbioSensorAdapter.dll</sensorAdapterLib>
         <engineAdapterLib>vcsWBFEngineAdapter.dll</engineAdapterLib>
         <storageAdapterLib>winbiostorageadapter.dll</storageAdapterLib>
         <indicatorSupported>0</indicatorSupported>
         <supportedModes>
             <supportedMode>0x01</supportedMode>
         </supportedModes>
         <supportedPurposes>
             <supportedPurpose>0x01</supportedPurpose>
             <supportedPurpose>0x02</supportedPurpose>
             <supportedPurpose>0x04</supportedPurpose>
         </supportedPurposes>
  </deviceInfo>
</bioTestConfiguration>
 ```
### Step Four: Modify the driver configuration inf
Biometric driver packages will need to be submitted to the new DevCenter portal to obtain the required Windows Hello signature and be uploaded to WU. Packages will need to include specific properties in the driver INF file to properly specify the adaptor dll's obtaining the digital signature. The following example demonstrates the formatting to obtain the bio signature on adaptor binaries and their related libraries.

For example, if the driver package contained a sensor, engine, and storage adaptor named sensor.dll, engine.dll, and storage.dll respectively, and one loaded stringparser.dll, then to obtain the bio signature on each one, the INF file would have to include the following components:

```cpp
[SignatureAttributes]
sensor.dll = SignatureAttributes.WindowsHello
engine.dll = SignatureAttributes.WindowsHello
storage.dll = SignatureAttributes.WindowsHello
stringparser.dll = SignatureAttributes.WindowsHello

[SignatureAttributes.WindowsHello]
WindowsHello = true
```

This step is the most important to making sure your driver receives the proper certification. All third party biometric adaptor files and any third party dlls loaded by these adaptors will need to be labeled and included in this manner if they are to obtain the biometric signature when submitted to DevCenter.

### Step Five: Run the HLK test suite
The HLK tests will make sure the above modifications have been made in steps 3 and 4 and will fail if the configurations information is not there.
When packaging the final HLK in HLK studio include the security review template submitted in the bug as a supplemental file.

### Step Six: Submit the driver package and HLK logs
Submit the packaged HLK file to DevCenter for review. The feature team within Microsoft will be notified of the submission when it reaches the manual review process. The team will review the submitted template in the HLK package to make sure the self-validated information meets the Microsoft’s biometric requirements.

### Step Seven: Wait for Microsoft approval and signing
Microsoft will approve the submission provided it meets all Biometric requirements
Obtaining the biometric signature is not certification that the driver will work with Windows Hello. For example, a file could be excluded in the inf configuration file that is checked for the signature. If this file is loaded at the time the OS enforces the signature, the load will fail and the driver will not operate with Windows Hello. The signed driver should be tested by the IHV and OEM to ensure it works in the collective system.

### Step Eight: Update an existing driver
If an update to a previously signed driver needs to be made, follow the instructions under step 3 for filling in the bugId and updateExistingSubmission fields in the driver configuration xml for the updated driver.
If an update is being made to a grandfathered driver, the same steps should be used. The bugId field should be set to the submission ID of the grandfathered driver and the updateExistingSubmission field should be set to true.
The driver configuration xml should be included in the driver package that is submitted.

## Related topics


[Windows Hello face authentication](/windows-hardware/design/device-experiences/windows-hello-face-authentication)

[Windows Hello](/windows-hardware/design/device-experiences/windows-hello)

[Biometric Devices Design Guide](./index.md)
