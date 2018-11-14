---
title: Standardized INF Keywords for Network Devices
description: Standardized INF Keywords for Network Devices
ms.assetid: F79AFB63-D404-4A5C-9515-82FFEB667048
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Standardized INF Keywords for Network Devices





This section provides information about standardized keywords that appear in the registry and are specified in INF files. NDIS 6.0 and later versions of NDIS support standardized keywords for miniport drivers in network devices.

Standardized keywords provide:

-   Standardized user interface properties for end users.

-   The ability for both home network users and large-scale enterprises to easily configure networks that include devices from multiple hardware manufacturers.

-   The ability to programmatically test for all advanced network device features.

The following standard INF keywords are mandatory for connectionless NDIS 6.0 and later miniport drivers:

-   **\*IfType**

-   **\*MediaType**

-   **\*PhysicalMediaType**

If the mandatory keywords are missing from the driver's INF file, NDIS does not call the miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function.

Standardized keywords are required for NDIS 6.0 and later miniport drivers if both of the following are true:

-   An INF setting must be exposed in the **Advanced** properties page of the user interface.

-   The device fully supports the specified properties.

**Note**  Standardized keywords are optional but recommended for NDIS 5.1 and earlier NDIS miniport drivers.

 

This section specifies the INF keywords that are exposed in the user interface. However, miniport drivers must read the registry settings during initialization to determine the current configuration settings.

Within an INF file, definitions for these keywords are placed with the other definitions for the advanced properties page. For more information about advanced properties, see [Specifying Configuration Parameters for the Advanced Properties Page](specifying-configuration-parameters-for-the-advanced-properties-page.md).

All standardized keyword names start with an asterisk (**\\***). This naming convention enables you to easily distinguish standardized names from non-standard names.

There are three types of standardized keyword data that are exposed in the user interface:

<a href="" id="enum"></a>Enum  
Values that can be selected from a list that appears in a drop down menu in the **Advanced** properties page.

<a href="" id="int"></a>Int  
Numerical values that you can edit.

<a href="" id="edit"></a>Edit  
Text values that you can edit.

The following topics include descriptions for the standardized keywords that are common to all networking technologies:

[Enumeration Keywords](enumeration-keywords.md)

[Keywords That Can Be Edited](keywords-that-can-be-edited.md)

[Keywords Not Displayed in the User Interface](keywords-not-displayed-in-the-user-interface.md)

In addition, standardized keywords that are specific to networking technologies are described in the following topics:

[INF File Settings for Filter Drivers](inf-file-settings-for-filter-drivers.md)

[INF Requirements for NDKPI](inf-requirements-for-ndkpi.md)

[MB Miniport Driver INF Requirements](mb-miniport-driver-inf-requirements.md)

[Standardized INF Keywords for Header-Data Split](standardized-inf-keywords-for-header-data-split.md)

[Standardized INF Keywords for NDIS Quality of Service (QoS)](standardized-inf-keywords-for-ndis-qos.md)

[Standardized INF Keywords for NDIS Selective Suspend](standardized-inf-keywords-for-ndis-selective-suspend.md)

[Standardized INF Keywords for NVGRE Task Offload](standardized-inf-keywords-for-nvgre-task-offload.md)

[Standardized INF Keywords for Packet Coalescing](standardized-inf-keywords-for-packet-coalescing.md)

[Standardized INF Keywords for Power Management](standardized-inf-keywords-for-power-management.md)

[Standardized INF Keywords for RSC](standardized-inf-keywords-for-rsc.md)

[Standardized INF Keywords for RSS](standardized-inf-keywords-for-rss.md)

[Standardized INF Keywords for Single Root I/O Virtualization (SR-IOV)](standardized-inf-keywords-for-sr-iov.md)

[Standardized INF Keywords for Virtual Machine Queue (VMQ)](standardized-inf-keywords-for-vmq.md)

 

 





