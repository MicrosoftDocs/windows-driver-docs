---
title: GDL Architecture
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
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 

 




