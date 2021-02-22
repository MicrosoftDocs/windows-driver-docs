---
title: Using an Extension INF File Template
description: Describes how to use extension INF templates
ms.topic: article 
ms.localizationpriority: medium
ms.date: 06/12/2020
---

# Using an Extension INF File Template

This page describes how to use extension INF templates to improve extensibility.

An extension INF template is an extension INF with entries commented out that a device manufacturer (IHV) publishes in a separate driver package. Typically, the IHV separates out optional features from the base INF and puts them in an extension INF template. In the template, the IHV provides comments indicating entries that the system builder (OEM) can uncomment and change, as well as entries which can be uncommented but should not be changed.  The OEM then uses the template as a starting point to create an extension INF.

To create an extension INF based on a template, follow the guidance in [Creating an extension INF](using-an-extension-inf-file.md#creating-an-extension-inf) and refer to the examples at the bottom of that page.

To submit a new extension INF that is based on a template, use the [DUA process](/windows-hardware/test/hlk/user/create-a-driver-only-update-package).

> [!NOTE]
> If an OEM uses the DUA process to modify an IHV-provided base INF, ownership of the base INF shifts to the OEM. Instead, the OEM should contact the IHV and request that appropriate extensibility be added to the base INF, or that the IHV provide an extension INF template.

An IHV might also use an extension INF template to add optional functionality to an already published driver package. By publishing a template rather than updating the base INF, the IHV helps ensure that existing extension INFs continue to work. The following sequence shows how this might work:

1. The IHV adds the new, optional value to an extension INF template, but not to the base INF.
2. The IHV adds code to the base driver to check for the existence of the new registry value:
    * If the updated base driver finds the new value, it uses the new functionality.
    * Otherwise, it uses the previous functionality.
3. The OEM uses the extension INF template to create a new extension INF that sets the new value.

If instead, the IHV decides to update the base INF, follow the guidelines described in [Using an Extension INF File](using-an-extension-inf-file.md#backward-compatibility).

## Related topics

* [Using an Extension INF file](using-an-extension-inf-file.md)
* [Working with Extension INFs in the Partner Center](../dashboard/submit-dashboard-extension-inf-files.md)