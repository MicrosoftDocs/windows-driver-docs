---
title: DSM Terminology
author: windows-driver-content
description: DSM Terminology
ms.assetid: 72a62672-b4bb-42f4-a80f-9aa4d60951ca
---

# DSM Terminology


The following terms will be helpful in understanding DSM for WSD:

<a href="" id="web-services-on-devices--wsd-"></a>**Web Services on Devices (WSD)**  
An implementation Microsoft technologies (including Devices Profile for Web Services) to support web services by a device. For more information about WSD, see [Web Services on Devices](http://go.microsoft.com/fwlink/p/?linkid=154858).

<a href="" id="devices-profile-for-web-services--dpws-"></a>**Devices Profile for Web Services (DPWS)**  
A specification that ties together WSD specifications to form a consistent set of requirements for a device to support web service content. The DPWS makes it easy for limited resource devices to support web services. For more information about DPWS, see [Introducing DPWS](http://go.microsoft.com/fwlink/p/?linkid=154859).

<a href="" id="distributed-scan-management--dsm-"></a>**Distributed Scan Management (DSM)**  
A distributed scanning system that combines the Microsoft Management Console (MMC) DSM component, the DSM scan server, and the DSM scanning device.

<a href="" id="dsm-device"></a>**DSM Device**  
A Web Services on Devices (WSD) device that supports Distributed Scan Management (DSM). This can be a scanner, a scanner component of a multifunction printer (MFP), or other scanning device.

<a href="" id="dsm-scan-server"></a>**DSM Scan Server**  
A computer that supports the Distributed Scan Management server component. Shipped in Windows 2008 R2.

<a href="" id="scan-process-"></a>**Scan Process**   
A set of instructions for acquiring and processing images. The instructions are created by an administrator. The term **Post-Scan Process (PSP)** applies to this definition as well.

<a href="" id="scan-job"></a>**Scan Job**  
A unit of work within the DSM device. It includes the Image Acquisition parameters (ScanTicket) and the scan documents.

<a href="" id="postscan-job"></a>**PostScan job**  
A unit of work within the DSM scan server**.** It includes the Post Processing instructions and the scan documents.

<a href="" id="control-point"></a>**Control Point**  
A component that implements the client side of a DSM web service.

<a href="" id="distributed-scan-device-web-service--ws-dsd-"></a>**Distributed Scan Device Web Service (WS-DSD)**  
A web service used by a **Control Point** to get status and configuration from a **DSM Device**.

<a href="" id="distributed-scan-processing-web-service--ws-dsp-"></a>**Distributed Scan Processing Web Service (WS-DSP)**  
A web service used by a **DSM Device** to create **PostScan Jobs** on a **DSM Scan Server**.

<a href="" id="distributed-scan-configuration-web-service--ws-dsc-"></a>**Distributed Scan Configuration Web Service (WS-DSC)**  
A web service used by a **Control Point** to get status and configuration from a **DSM Scan Server**. For more information, see [Scan Repository Capabilities and Status Retrieval Protocol Specification.](http://go.microsoft.com/fwlink/p/?linkid=154735)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20DSM%20Terminology%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


