---
title: GDL Architecture
author: windows-driver-content
description: GDL Architecture
ms.assetid: 3e796218-ab2a-40a7-a0e3-caeec5c6656e
keywords:
- GDL WDK , architecture
- creating snapshots WDK GDL
- snapshots WDK GDL , creating snapshots
- parser WDK GDL , accessing parser through IPrintCoreHelperUni
- GDL WDK , schemas
- GDL WDK , snapshots
- architecture WDK GDL
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GDL Architecture


This topic describes the architecture of the Generic Descriptor Language (GDL).

For each GDL data set, you should define a [GDL schema](gdl-schemas.md) to describe the format of data. Each file that contains a data set references the GDL schema. This schema allows the GDL parser to verify that the data set conforms to the schema and to perform any specified transformations when the snapshot is constructed. For all data that is defined in the GPD, Microsoft has provided a standard schema. In addition, the parser enables you to define some data as configurable. Other data can be described in a manner that makes it depend on the configuration that is used.

The specification can be converted into a GDL schema. Each file that contains a data set references the GDL schema. This schema enables the GDL parser to verify that the data set conforms to the schema and to perform any specified transformations when the snapshot is constructed.

After the data sets and the schema are defined, the client can create multiple views, or [snapshots](gdl-snapshots.md), from a single data set by specifying different configurations. For Unidrv configuration and rendering plug-ins, the client can access the snapshot through the methods in the [IPrintCoreHelperUni](https://msdn.microsoft.com/library/windows/hardware/ff552940) interface.. The GDL parser will load the schema that is specified in the data set and verify that the data set conforms to its schema. If the data set does not conform, the parser will indicate a failure to parse the file.

After the data sets and the schema have been defined, the client can create snapshots of a data set by specifying a configuration:

1.  The plug-in obtains a pointer to the **IPrintCoreHelperUni** interface through the [**IPrintOemUI::PublishDriverInterface**](https://msdn.microsoft.com/library/windows/hardware/ff554184) method.

2.  The plug-in requests access to the snapshot through a call to either [**IPrintCoreHelperUni::CreateGDLSnapshot**](https://msdn.microsoft.com/library/windows/hardware/ff552923) or [**IPrintCoreHelperUni::CreateDefaultGDLSnapshot**](https://msdn.microsoft.com/library/windows/hardware/ff552917). If the plug-in calls **CreateGDLSnapshot**, the caller provides a DEVMODE structure that includes the configuration that the parser uses to determine the view of the snapshot.

3.  The GDL parser loads the schema that is specified in the data set and verifies that the data set conforms to its schema. If the data set does not conform, error messages will be issued.

4.  The GDL parser creates an internal data structure from the GDL source file and determines the appropriate view based on the configuration that is provided and processing instructions in the schema.

5.  The parser creates an XML representation (the *snapshot*) of the processed data entries. This XML snapshot is returned to the plug-in as a stream..

If a schema is omitted, the parser will simply perform schema validation and the snapshot values will be represented in the snapshot as the string of bytes that were originally defined in the GDL source file.

**Note**   The **PublishDriverInterface** method is part of the **IPrintOemUni** interface and other interfaces as well. So a plug-in does not necessarily get the helper interface from [**IPrintOemUI::PublishDriverInterface**](https://msdn.microsoft.com/library/windows/hardware/ff554184). It can get the helper interface from **IPrintOemUni::PublishDriverInterface** or elsewhere depending on the type of interface that the plug-in implements.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Architecture%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


