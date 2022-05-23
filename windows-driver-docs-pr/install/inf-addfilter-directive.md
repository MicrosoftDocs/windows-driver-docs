---
title: INF AddFilter Directive
description: An AddFilter directive describes the installation a driver service as a filter driver.
ms.date: 05/11/2022
---

# INF AddFilter Directive

Each **AddFilter** directive describes the installation of a driver service as a declarative filter into either a filter position or level.  This directive is supported in Windows 10 version 1903 and later.

Rather than use a registry value to specify a specific list of upper or lower filters to be added to the device stack, declarative filters registers filters using metadata.  This metadata is this used to generate the final list of filters at the time the device is started.  Declarative filters can be used in conjunction with the legacy model of using the UpperFilters/LowerFilters registry values.  For more information on the declarative filter model, please see [Device filter driver ordering](/windows-hardware/drivers/develop/device-filter-driver-ordering).

An **AddFilter** directive is used within an [**INF *DDInstall*.Filters**](inf-ddinstall-software-section.md) section.

```inf
[DDInstall.Filters]
AddFilter=FilterName,[flags],filter-install-section
```

## Entries

*FilterName*

Specifies the name of the filter to be installed.  This name must exactly match the name of a driver service installed on the system.

*flags*

Flags are currently unused and must be 0 if specified.

*filter-install-section*

References an INF-writer-defined section that contains metadata about how the filter should be added to the device stack.
	
## Remarks

Each INF-writer-created section name must follow the general rules for defining section names.  For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

An **AddFilter** directive must reference a named *filter-install-section* elsewhere in the INF file.  Each such section has the following form:

```inf
[filter-install-section]

[FilterLevel = LevelName]
[FilterPosition = Upper / Lower]
```

>[!NOTE]
>In each *filter-install-section*, either the filter position or the filter level must defined, but not both.  See [device filter driver ordering](/windows-hardware/drivers/develop/device-filter-driver-ordering) for full details on defining filter metadata

### [filter-install-section]: FilterLevel

`FilterLevel = {LevelName}`

**FilterLevel** specifies the name of a filter level defined by the [base driver package](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/using-an-extension-inf-file) of the device.  The filter is registered with that level name, and the final list of filters is determined when the device starts by assembling the filter list from the registered filters in accordance with the filter level metadata supplied by the base driver package.  In the event that the specified filter level is not defined in the base driver package's metadata, the filter is not added to the stack.

For full details on the process of defining the filter level metadata and how the final filter list is assembled, see [device filter driver ordering](/windows-hardware/drivers/develop/device-filter-driver-ordering).

### [filter-install-section]: FilterPosition

`FilterPosition = {Upper / Lower}`

**FilterPosition** specifies the position of a filter on the stack, as either an upper or lower filter.  If the base driver package of the device specifies filter level metadata, using **FilterPosition** will insert the filter into the default filter level for either the upper or lower device filters, as specified.  If the base driver package does not supply this metadata, then the filter will be inserted into the specified upper or lower filters in effectively arbitrary order.

## See Also

[Device filter driver ordering](/windows-hardware/drivers/develop/device-filter-driver-ordering)
