---
title: Creating a mobile package
description: This topic provides information about creating a package for installing the sample driver on a mobile device.
ms.assetid: E929D80D-17BF-4079-8CF9-972020306358
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Creating a mobile package


This topic provides information about creating a package for installing the sample driver on a mobile device.

Perform the following tasks to create a package for the sample driver.

1. Copy the following code and paste it into Notepad.

```XML
<?xml version="1.0" encoding="utf-8"?>
<!--
Copyright (c) Microsoft Corporation.  All rights reserved.
-->
<Package xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"
  Owner="OEMName"
  OwnerType="OEM"
  Component="Drivers"
  SubComponent="Adxl345Acc"
  ReleaseType="Production"
  xmlns="urn:Microsoft.WindowsPhone/PackageSchema.v8.00">
  <Components>
    <OSComponent>
      <Files>
        <File DestinationDir="$(runtime.drivers)\umdf" Source="$(_RELEASEDIR)\Adxl345Acc.dll" />
      </Files>

      <RegKeys>
        <RegKey KeyName="$(hklm.system)\ControlSet001\Enum\Root\umdf2\Adxl345Acc">
          <RegValue Name="ClassGUID"    Type="REG_SZ"        Value="{5175D334-C371-4806-B3BA-71FD53C9258D}"  />
          <RegValue Name="Class"        Type="REG_SZ"        Value="Sensor" />
          <RegValue Name="ConfigFlags"  Type="REG_DWORD"     Value="00000020"  />
          <RegValue Name="HardwareID"   Type="REG_MULTI_SZ"  Value="umdf2\Adxl345Acc"  />
        </RegKey>
      </RegKeys>
    </OSComponent>

    <!-- Use Phone-specific INF for security. -->
    <Driver InfSource="$(DRIVERS_FILES_PATH)\Adxl345Acc.inf">
      <Security InfSectionName="Sensor_Inst_SecurityAddReg">
          <AccessedByCapability Id="ID_CAP_SENSORS" Rights="$(GENERIC_READ)$(GENERIC_EXECUTE)" />
      </Security>
      <Reference Source="$(_RELEASEDIR)\Adxl345Acc.dll" />
    </Driver>

  </Components>

</Package>
```

>[!NOTE]
> The value of the **Security InfSectionName** element must be exactly the same as the value of the **AddReg** field discussed in this topic: [Review the INX file](review-and-revise-the-inf-file.md).

 

2. In the main menu in Notepad, click **File** &gt; **Save As**, then in the **Save As** dialog window, use the dropdown box to set the **Save as type** field to **All Files**.****

3. In the **File name** text box, type the following:

*adxl345acc.pkg.xml*
4. Use the destination box at the top of the **Save As** dialog window to navigate to the project folder in Microsoft Visual Studio. Then click **Save**.

After creating the *adxl345acc.pkg.xml* file as shown in the preceding steps, you can also use the **pkggen.exe** tool that's included with the Windows Driver Kit (WDK), to package the file.

If you installed the WDK to the default location, then you can find **pkggen.exe** in the following location:

*%SystemRoot%\\Program Files (x86)\\Windows Kits\\10\\Tools\\bin\\i386*
Refer to [Run the pkggen.exe tool](https://msdn.microsoft.com/windows/hardware/dn756642.aspx#run-pkg), for instructions on how to create a package for your mobile device. And see [Creating mobile packages](https://msdn.microsoft.com/windows/hardware/dn756642.aspx) for a more comprehensive introduction.

## Related topics
[Creating mobile packages](https://msdn.microsoft.com/windows/hardware/dn756642.aspx)
[Review the INX file](review-and-revise-the-inf-file.md)
[Run the pkggen.exe tool](https://msdn.microsoft.com/windows/hardware/dn756642.aspx#run-pkg)



