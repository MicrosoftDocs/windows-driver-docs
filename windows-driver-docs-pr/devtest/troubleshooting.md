---
title: Troubleshooting the Metadata Authoring Wizards
description: Troubleshooting the metadata authoring wizards
keywords:
- Troubleshooting the Metadata Authoring Wizard
ms.date: 04/20/2017
---

# Troubleshooting the metadata authoring wizards

This topic describes the Device Metadata Authoring tool provided in the Windows Driver Kit (WDK) 8.

If you receive any of the following error messages, refer to the Resolution column in the table to resolve the issue.

|Tool|Screen|Error message|Resolution|
|----|----|----|----|
|Metadata Authoring Wizard|Welcome|ERROR: You must specify a folder location|Enter a folder path.|
|Metadata Authoring Wizard|Welcome|ERROR: FolderLocation.Text folder does not exist|Correct the file path.|
|Metadata Authoring Wizard|Welcome|The chosen file doesn't exist|Correct the file path or name.|
|Metadata Authoring Wizard|Welcome|XML File error|Correct the XML error.</br>**Error examples:**</br></br>Was expecting the first child of {0} to be {1}, but found {2} instead.</br></br>Was expecting {0} to be followed by {1}, but found {2} instead.|
|Metadata Authoring Wizard|Finish|Package creation failed:|Change the parameter based on the instructions.</br>**Error examples:**</br></br>You must specify the ModelName for the device (locale {0})</br></br>You must associate this package with at least one HardwareID or ModelID</br></br>You must specify a primary category for this device.</br></br>**Warning examples:**</br></br>ModelNumber ({0}) is not specified</br></br>DeviceDescription 2 ({0}) is not specified</br></br>The generic icon will be determined by the primary category selection|
|Metadata Authoring Wizard|Association|Invalid format : "Value" - don't add { } in the beginning and end.|Remove the {} and try again.|
|Metadata Authoring Wizard|Association|Invalid GUID format: "Value"|Type the correct GUID and try again.|
|Metadata Authoring Wizard|Icon|There were problems with the icon file: "Error Message" Icon Validation Error|The icon can't be found or doesn't meet the requirement to be displayed in Devices and Printers in Control Panel. Find or fix the icon and try again.</br></br>**Error examples:**</br></br>Error: Image 256x256 transparency needs to be set.</br></br>Error: Image 48x48:32bit+Alpha does not exist.|
|Submission Wizard|Select metadata packages|There is already a package with that name in the list|Create a new GUID for the device metadata package.|
|Submission Wizard|Select metadata packages|There was a problem loading the package:|Change the parameter based on the instructions.|
|Submission Wizard|Finish|There was a problem creating the submission package:|Change the parameter based on the instructions.|
