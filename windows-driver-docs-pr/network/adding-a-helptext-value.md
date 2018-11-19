---
title: Adding a HelpText Value
description: Adding a HelpText Value
ms.assetid: fb29852c-5d47-4660-9fe4-dc8ae05449ff
keywords:
- add-registry-sections WDK networking , HelpText values
- HelpText values WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding a HelpText Value





The INF file for a **NetTrans**, **NetClient**, or **NetService** network component that is visible in a user interface should add a **HelpText** value (REG\_SZ) to the component's **Ndi** key.

**Note**  **NetClient** components are deprecated in Windows 8.1, Windows Server 2012 R2, and later.

 

The **HelpText** value is a localizable string that explains how the component benefits the user. For example, the **HelpText** value for a **NetClient** component should not simply identify the client but indicate what the client allows the user to connect to. The **HelpText** value is displayed at the bottom of the **General** page of the **Connection Properties** dialog box when a component on the page is selected.

**Note**  Net components (adapters) and IrDA components do not support a **HelpText** value.

 

The following is an example of an *add-registry-section* that adds a **HelpText** value to the **Ndi** key:

```INF
[MS_Protocol.ndi_reg]
HKR, Ndi, HelpText, 0, %MyTransport_Help%
```

The **HelpText** value is a % *strkey*% token that is defined in the **Strings** section of the INF file. For more information about the **Strings** section, see the [**INF Strings Section**](https://msdn.microsoft.com/library/windows/hardware/ff547485).

**Note**  For Multilingual User Interface (MUI) support, the **HelpText** value can be an indirect string in the form `@filename,resource`. For example: "@%SystemRoot%\\System32\\drivers\\mydriver.sys,-1000". The target string is located in the specified file. The resource value identifies the specific string within the file. If the resource value is zero or greater, the number is used as an index of the string in a binary file. If the resource value is negative, it is used as a resource identifier in a resource file.

 

 

 





