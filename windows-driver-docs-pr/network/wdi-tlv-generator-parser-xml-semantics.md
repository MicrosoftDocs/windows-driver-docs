---
title: WDI TLV generator/parser XML semantics
description: The TLV generator/parser XML file is a list of messages, containers (TLVs), and property groups (structs). This topic covers the XML syntax.
ms.assetid: AD268E68-B969-45D8-A2F2-4025E827D496
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDI TLV generator/parser XML semantics


The TLV generator/parser XML file is a list of messages, containers (TLVs), and property groups (structs). This topic covers the XML syntax.

-   [`<message />`](#-message---)
    -   [Attributes](#attributes)
    -   [Content](#content)
    -   [Example](#example)
-   [`<containerRef />`](#-containerref---)
    -   [Attributes](#attributes)
    -   [Content](#content)
    -   [Example](#example)
-   [`<containers />`](#-containers---)
-   [`<container />`](#-container---)
    -   [Attributes](#attributes)
    -   [Contents](#contents)
    -   [Example](#example)
-   [`<groupRef />`](#-groupref---)
    -   [Attributes](#attributes)
    -   [Content](#content)
    -   [Examples](#examples)
-   [`    <namedType />`](#--namedtype---)
    -   [Attributes](#attributes)
    -   [Content](#content)
    -   [Example](#example)
-   [`<aggregateContainer />`](#-aggregatecontainer---)
    -   [Attributes](#attributes)
    -   [Content](#content)
    -   [Example](#example)
-   [`<propertyGroups />`](#-propertygroups---)
-   [Primitive Field Types (`<bool/> <uint8/> <uint16/> <uint32/> <int8/> <int16/> <int32/>`)](#primitive-field-types---bool----uint8----uint16----uint32----int8----int16----int32---)
    -   [Attributes](#attributes)
    -   [Contents](#contents)
-   [`<propertyGroup />`](#-propertygroup---)
    -   [Attributes](#attributes)
    -   [Contents](#contents)
    -   [Example](#example)

## `<message />`


Describes a single top-level WDI message. There are only parser/generator functions for these message entries.

### Attributes

-   `commandId` - Symbolic constant that must be defined in dot11wdi.h.
-   `type` - Type name to be exposed to the code (you use this type when calling into parser/generator functions).
-   `description` - Description of the command.
-   `direction` – Indicates whether this message describes the TLV stream as it goes from WDI to the IHV miniport as part of an M1 (called "ToIhv"), describes the TLV stream as it goes from the IHV miniport to WDI as an M0, M3, or M4 (called "FromIhv"), or it goes in both directions (called "Both"). See *Message Direction* in [WDI TLV parser interface overview](wdi-tlv-parser-interface-overview.md).

### Content

List of container references (`<containerRef />`). These are the different TLVs that make up the message. They are references to types defined in the `<containers />` section.

### Example

```XML
<message commandId="WDI_SET_P2P_LISTEN_STATE"
         type="WDI_SET_P2P_LISTEN_STATE_PARAMETERS"
         description="Parameters to set listen state."
         direction="ToIhv">
  <containerRef id="WDI_TLV_P2P_CHANNEL_NUMBER"
                name="ListenChannel"
                optional="true"
                type="WFDChannelContainer" />
  <containerRef id="WDI_TLV_P2P_LISTEN_STATE"
                name="ListenState"
                type="P2PListenStateContainer" />
</message>
```

## `<containerRef />`


Reference to a `<container />` defined in the `<containers />` section.

### Attributes

-   `id` - TLV ID that must be defined in wditypes.h.
-   `name` - The name of the variable in the parent structure.
-   `optional` - Specifies whether or not it is an optional field. False by default. Generated code enforces "optional-ness".
-   `multiContainer` – Specifies whether or not the generated code should expect multiple TLVs of the same type. False by default. If false, generated code enforces that only one is present.
-   `type` - Reference to a specific element’s "name" attribute in the `<containers />` section.
-   `versionAdded` - Part of versioning. Indicates that this TLV container should not appear in byte streams to/from peers with a version less than the one indicated in this attribute.
-   `versionRemoved` - Part of versioning. Indicates that this TLV container should not appear in byte streams to/from peers with a version greater than or equal to the one indicated in this attribute.

### Content

None.

### Example

```XML
<containerRef id="WDI_TLV_P2P_CHANNEL_NUMBER"
              name="ListenChannel"
              optional="true"
              type="WFDChannelContainer"/>
```

## `<containers />`


Describes all containers/TLVs used in WDI messages. Containers can be considered TLV buckets. There are 2 types: `<container />` and `<aggregateContainer />`.

## `<container />`


TLV Container for a single structure reference or named type. It is statically sized, but may be a C-style array as long as it is statically sized.

### Attributes

-   `name` - ID that is referenced by WDI messages/other containers.
-   `description` - Friendly description of what the container is for.
-   `type` – Type name to be exposed to the code.
-   `isCollection` - Specifies whether or not generated code should expect many of the same size element within the same TLV (C-style array). The default is false (only expect one element of the given type).
-   `isZeroValid` - Only valid when `isCollection` is true. Determines whether a zero element array is allowed. This is useful when the TLV stream needs to distinguish between an optional TLV that is not present versus one that is present but has zero length (like SSIDs). Since this distinction is rare, the default is false.

### Contents

One of `<groupRef />` or `<namedType />`.

### Example

```XML
<container name="P2PListenStateContainer"
           description="Container for P2P Listen State setting."
           type="WDI_P2P_LISTEN_STATE_CONTAINER">
  <namedType name="ListenState"
             type="WDI_P2P_LISTEN_STATE"
             description="P2P Listen State."/>
</container>
```

## `<groupRef />`


Reference to a property group (structure) defined in the `<propertyGroups />` section.

### Attributes

-   `name` - Name of the structure in the parent structure.
-   `ref` - Reference to a named structure in a `<propertyGroups />` section.
-   `description` – Friendly descriptor of what the structure is used for.

### Content

None.

### Examples

```XML
<container name="WFDChannelContainer"
           description="Container for a Wi-Fi Direct channel."
           type="WDI_P2P_CHANNEL_CONTAINER">
  <groupRef name="Channel"
            ref="WFDChannelStruct"
            description="Wi-Fi Direct Channel." />
</container>
```

## ` <namedType />`


Reference to a raw type exposed by wditypes.hpp or dot11wdi.h. Uses default serializer (memcpy), so use at your own risk because of padding issues.

### Attributes

-   `name` - Name of the structure in the parent structure.
-   `type` - Type name to use in the actual code.
-   `description` – Friendly description of what the structure is used for.

### Content

None.

### Example

```XML
<container name="P2PListenStateContainer"
           description="Container for P2P Listen State setting."
           type="WDI_P2P_LISTEN_STATE_CONTAINER">
  <namedType name="ListenState"
             type="WDI_P2P_LISTEN_STATE"
             description="P2P Listen State."/>
</container>
```

## `<aggregateContainer />`


TLV Container for many different containers. This is used for handling nested TLVs.

### Attributes

-   `name` - ID that is referenced by WDI messages/other containers.
-   `description` – Friendly description of what the container is for.
-   `type` - Type name to be exposed to the code.

### Content

List of `<containerRef />`.

### Example

```XML
<aggregateContainer
    name="P2PInvitationRequestInfoContainer"
    type="WDI_P2P_INVITATION_REQUEST_INFO_CONTAINER"
    description="Generic container for Invitation Request-related containers.">
  <containerRef
    id="WDI_TLV_P2P_INVITATION_REQUEST_PARAMETERS"
    type="P2PInvitationRequestParamsContainer"
    name="RequestParams" />
  <containerRef
    id="WDI_TLV_P2P_GROUP_BSSID"
    type="MacAddressContainer"
    name="GroupBSSID"
    optional="true" />
  <containerRef
    id="WDI_TLV_P2P_CHANNEL_NUMBER"
    type="WFDChannelContainer"
    name="OperatingChannel"
    optional="true" />
  <containerRef
    id="WDI_TLV_P2P_GROUP_ID"
    type="P2PGroupIDContainer"
    name="GroupID" />
</aggregateContainer>
```

## `<propertyGroups />`


Describes all structures used in all containers. Structures can either be used by a `<container />`, or referenced by another `<propertyGroup />` (nested structures). They are defined independently of TLVs containers so they can be re-used. They do not have a TLV header.

These definitions are necessary as they help to solve padding issues with structures and gives the code generator instructions on how to interpret the data.

**Note**  Order matters here. All data offsets are implied based on the property group description, and data is written/parsed in the order it is defined here. These structures have to be defined here.

 

## Primitive Field Types (`<bool/> <uint8/> <uint16/> <uint32/> <int8/> <int16/> <int32/>`)


These are the available primitive types, and are converted/marshalled appropriately by the generated code.

### Attributes

-   `name` - Field name in the parent structure.
-   `description` – Friendly description of what the property is for.
-   `count` - How many of the given property there are. Default is one. Values greater than one make this property into a statically sized array in the code.

### Contents

None

## `<propertyGroup />`


An individual structure.

### Attributes

-   `name` - ID that is referenced by WDI messages/other containers.
-   `description` – Friendly description of what the property group is for.
-   `type` - Type name to be exposed to the code.

### Contents

There are several possible property types (struct fields).

-   `<bool/> <uint8/> <uint16/> <uint32/> <int8/> <int16/> <int32/>`

-   `<groupRef />`

-   `<namedType />`

### Example

```XML
<propertyGroup name="P2PDiscoverModeStruct"
               type="WDI_P2P_DISCOVER_MODE"
               description="Structure definition for P2P Discover Mode Parameters">
  <namedType name="DiscoveryType"
             type="WDI_P2P_DISCOVER_TYPE"
             description="Type of discovery to be performed by the port."/>
  <bool name="ForcedDiscovery"
        description="A flag indicating that a complete device discovery is required. If this flag is not set, a partial discovery may be performed." />
  <namedType name="ScanType"
             type="WDI_P2P_SCAN_TYPE"
             description="Type of scan to be performed by port in scan phase." />
  <bool name="ScanRepeatCount"
        description="How many times the full scan procedure should be repeated. If set to 0, scan should be repeated until the task is aborted by the host."/>
</propertyGroup>
<propertyGroup name="P2PDeviceInfoParametersStruct"
               type="WDI_P2P_DEVICE_INFO_PARAMETERS"
               description="Structure definition for P2P Device Information Parameters.">
  <uint8 count="6"
         name="DeviceAddress"
         description="Peer&#39;s device address." />
  <uint16 name="ConfigurationMethods"
          description="Configuration Methods supported by this device." />
  <groupRef name="DeviceType"
            description="Primary Device Type."
            ref="WFDDeviceType" />
</propertyGroup>
```

 

 





