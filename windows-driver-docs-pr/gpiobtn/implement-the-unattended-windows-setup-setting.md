---
title: Implement the Unattended Windows Setup Setting
description: This topic describes how to set the unattended Windows Setup component setting.
ms.date: 10/17/2018
---

# Implement the unattended Windows Setup setting


This topic describes how to set the unattended Windows Setup component setting.

We strongly recommend that you use [Windows System Image Manager](/previous-versions/windows/it-pro/windows-vista/cc722301(v=ws.10)) to edit the Windows Setup unattended file.

The following is a sample output file:

``` syntax
<unattend xmlns="urn:schemas-microsoft-com:unattend">
  <settings pass="specialize">
    <component
        name="Microsoft-Windows-GPIOButtons"
        processorArchitecture="x86"> <!-- ... Additional component attributes-->
      <ConvertibleSlateMode>1</ConvertibleSlateMode> <!-- Values: {0 (slate); 1 (laptop)}-->
    </component>
  </settings>
</unattend>
```

 

