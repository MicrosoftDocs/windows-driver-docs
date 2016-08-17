---
title: Mapping PTP Associations to WIA Folders
description: Mapping PTP Associations to WIA Folders
MS-HAID:
- 'WIA\_drv\_cam\_a098b202-a9d9-4d83-814c-e75500fff0d2.xml'
- 'image.mapping\_ptp\_associations\_to\_wia\_folders'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 81de26fd-1f93-4018-a628-ad0b0d7468ba
---

# Mapping PTP Associations to WIA Folders


## <a href="" id="ddk-mapping-ptp-associations-to-wia-folders-si"></a>


For most object associations, the PTP driver creates a WIA folder item. The WIA\_IPA\_ITEM\_FLAGS property has different flags set, depending on the association type, as shown in this table:

PTP Association Code
Association Type
WIA Item Type Flags
(described in the Windows SDK documentation)
0x0000

Undefined

WiaItemTypeFolder

0x0001

GenericFolder

WiaItemTypeFolder

0x0002

Album

WiaItemTypeFolder

0x0003

TimeSequence

WiaItemTypeFolder | WiaItemTypeBurst

0x0004

HorizontalPanoramic

WiaItemTypeFolder | WiaItemTypeHPanorama

0x0005

VerticalPanoramic

WiaItemTypeFolder | WiaItemTypeVPanorama

0x0006

2DPanoramic

WiaItemTypeFolder

0x0007

AncillaryData

See accompanying text.

 

The **SequenceNumber** field of the ObjectInfo dataset is put into the WIA\_IPC\_SEQUENCE property. The PTP driver does not currently use the WIA\_IPC\_XCOORDINATE and WIA\_IPC\_YCOORDINATE properties. The **AssociationDesc** member of the ObjectInfo dataset is currently not used.

The following diagram shows an example AncillaryData association as stored on the camera. This association consists of an image together with associated audio and text.

![ptp tree for an image with ancillary data](images/ptp.png)

When an AncillaryData association is mapped to a WIA folder, the nonimage objects become children of the image object, as shown in the following diagram. The image object has the WiaItemTypeHasAttachments flag set in WIA\_IPA\_ITEM\_FLAGS.

![wia item with attachments](images/wiaattch.png)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Mapping%20PTP%20Associations%20to%20WIA%20Folders%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




