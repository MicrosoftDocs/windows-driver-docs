---
title: Audio Hardware Resource Management
description: Windows 10 includes the ability to express concurrency constraints using and XML file.
ms.date: 12/03/2021
---

# Audio Hardware Resource Management

Windows 10 includes the ability to express concurrency constraints using an XML file. On resource constrained device the ability to specify priority for specific audio streams can enhance the customer experience.

One challenge with creating a good audio experience on a low cost laptop or tablet device, is that some devices have various concurrency constraints. For example, it is possible that the device can only play up to 6 audio streams concurrently and supports only 2 offload streams. When there is an active video call with real time audio, it is possible that the device supports only 2 audio streams. When the device is capturing audio, the device can only play up to 4 audio streams.

Windows 10 includes a mechanism to express concurrency constraints to insure that high-priority audio streams will be able to play. If the system does not have enough resources, then low priority streams are terminated. 

Windows 11 provides additional capabilities with the use of *resource groups* and are covered later in this topic in [Resource Groups - Extended Audio Resource Management](#resource-groups---extended-audio-resource-management). 

To specify constraints complete these two steps.

- Create a concurrency constraints XML file as described in [Specify Concurrency Constraints](#specify-concurrency-resource-constraints).
- Configure a registry entry to use the custom concurrency constraints XML file as described in [Registry Key Configuration](#registry-key-configuration).

## Specify Concurrency Resource Constraints

The XML constraints file is made up of three sections. The first required section is defined by &lt;Limits&gt; &lt;/Limits&gt;. This section can be used to define up to fifteen resource restraints. For example you could define constraints for the maximum number of rendering stream and the maximum number of streams that can be offloaded.

```xml
<?xml version="1.0" encoding="utf-8"?>
<ConstraintModel>
  
  <Limits>
    <Resource>
      <ID>MaxRender</ID>
      <Consumption>6</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOffLoad</ID>
      <Consumption>2</Consumption>
    </Resource>
    ...

  </Limits>
```

The next section of the XML file defines one or more lists of exclusive endpoints, with each list containing two or more endpoints. These are endpoints that, that cannot be active at the same time. This section is optional.

For example, if the audio hardware has both HandsetSpeaker and WiredHeadsetSpeaker wired to the same DAC, that cannot be active at the same time, these should be in the same ExclusiveEndpoints list.

This section can have multiple &lt;ExclusiveEndpoints&gt; nodes. Each ExclusiveEndpoints node contains two or more Endpoint nodes. Each Endpoint node contains HWID, TopologyName, and PinId.

```xml
  <ExclusiveEndpoints>
    <Endpoint>
      <HWID>Root\sysvad_PhoneAudioSample</HWID>
      <!-- Example of h/w id specified in phoneaudiosample.inf -->
      <TopologyName>TopologySpeaker</TopologyName>
      <!-- Topology filter reference string-->
      <PinId>1</PinId>
      <!-- KSPIN_TOPO_LINEOUT_DEST -->
    </Endpoint>
    <Endpoint>
      <!-- Example of h/w id specified in phoneaudiosample.inf -->
      <HWID>Root\sysvad_PhoneAudioSample</HWID>
      <!-- Topology filter reference string-->
      <TopologyName>TopologyHandsetSpeaker</TopologyName>
      <!-- KSPIN_TOPO_LINEOUT_DEST -->
      <PinId>1</PinId>
    </Endpoint>
  </ExclusiveEndpoints>
```

The next section of the XML file defines various resource consumers. This section of the file contains multiple &lt;ResourceConsumer&gt; entries. Each entry identifies information about a resource consumer and their associated resources use. Each resource that is used, must be previously defined in the &lt;Limits&gt; section.

```xml
  <ResourceConsumer>
    <!-- Active Phone call -->
    <ConsumerInfo>
      <PhoneCall>
        <CallState>Active</CallState>
      </PhoneCall>
    </ConsumerInfo>
    <Resource>
      <ID>MaxRender</ID>
      <Consumption>2</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOffLoad</ID>
      <Consumption>2</Consumption>
    </Resource>
    ...
  </ResourceConsumer>
```

As audio resources are used, the audio service tracks the resources. When insufficient resources are available, either lower priority streams are terminated or the current resource request fails if existing resource consumers are higher priority.

These are the valid &lt;ConsumerInfo&gt; entries.

- &lt;PhoneCall&gt; - The &lt;Phonecall&gt; node contains a with CallState child node, that can be "Active" or "Hold".
- &lt;Stream&gt; - Audio streams. The &lt;Stream&gt; node contains the following child nodes.

    &lt;HWID- The hardware ID (hw-id) of the resource consumer as specified in the driver’s INF file.

    &lt;TopologyName&gt; - The topology filter reference string of the resource consumer.

    &lt;PinId&gt; - The pin ID of the resource consumer.

    &lt;Mode&gt; - The GUID of the associated mode. For more information, see [Audio Signal Processing Modes](audio-signal-processing-modes.md).

    &lt;ConnectorType&gt; - The connector type of the resource consumer. Valid values are: Host, Loopback, or Offload.

- &lt;KeywordDetector&gt; - Keyword detector used to support keyword trigger voice interactions.

The following table summarizes the render audio stream priorities, listed from highest to lowest priority.

| Render audio stream      | Priority |
|--------------------------|----------|
| Communications           | 1        |
| Game Chat                | 2        |
| Screen Reader            | 3        |
| Camera Shutter           | 4        |
| Push To Talk             | 5        |
| In Call Notification     | 6        |
| Personal Assistant       | 6        |
| Speech                   | 7        |
| Ringtone                 | 8        |
| Alarm                    | 9        |
| Movie                    | 10       |
| Foreground Only Media    | 10       |
| Background Capable Media | 11       |
| Media                    | 11       |
| Sound Effects            | 12       |
| DTMF                     | 12       |
| Game Media               | 12       |
| System                   | 12       |
| Game Effects             | 12       |
| Other                    | 13       |
| Alerts                   | 14       |

The following table summarizes the capture audio stream priorities, listed from highest to lowest priority.

| Capture audio stream     | Priority |
|--------------------------|----------|
| Communications           | 1        |
| Game Chat                | 2        |
| Push To Talk             | 4        |
| Personal Assistant       | 6        |
| Speech                   | 7        |
| Background Capable Media | 8        |
| Media                    | 8        |
| Other                    | 13       |
| Game Media               | 15       |
| Screen Reader            | 15       |
| Alerts                   | 15       |
| Foreground Only Media    | 15       |
| Game Effects             | 15       |
| Sound Effects            | 15       |
| DTMF                     | 15       |
| In Call Notification     | 15       |
| Alarm                    | 15       |
| Camera Shutter           | 15       |
| Movie                    | 15       |
| Ringtone                 | 15       |
| System                   | 15       |

### Examples

- Example 1: The user is talking over Skype, using Communications Render and Capture streams. They start a game, which attempts to create a Game Effects stream. If there aren’t enough resources available, the Game Effects stream creation will fail.

- Example 2: The user is playing music. They start an application that creates a Speech stream. If there aren’t enough resources available, the music stream will be terminated and the Speech stream creation will succeed.

## Wildcard Option for TopologyName 

A wildcard option is available for use with the TopologyName tag. This feature can be used to support the dynamic behavior associated with sideband Bluetooth. This option allows the audio driver to create a new set of interfaces for every paired bluetooth peripheral that match a specific pattern. This keeps the user settings for different audio peripherals from being mixed together. 

To do this, it is recommend adding the peripheral hardware id to the audio interface reference string. This can be accomplished by using a hash of the symbolic link for the peripheral. The audio driver Sysvad sample code includes  example implementations for HFP sideband, A2DP sideband, and USB sideband. The example functions are named "CreateFilterNames". This function hashes the symbolic link and combines that with the filter names, to generate the unique filter names for each peripheral.

The resource XML definitions are part of the driver package, and the hardware id's are unknown at the time it is created. 

To support this dynamic matching, an asterisk '*' wildcard option is provided for the last character in the resource XML declaration of the topology name. 

### Example Wildcard TopologyName 

For example, the actual interface reference string could be "BTHFPCapture-00AABBCCDD" and the corresponding entry in the resource XML would be `<TopologyName>BTHFPCapture-*</TopologyName>`. 

All endpoints created by the driver following the "BTHFPCapture-*" pattern would use the same resource definition.

## Resource Groups - Extended Audio Resource Management

Resource groups are available starting in Windows 11.  Resource groups allow endpoints to be assigned to different resource groups that are predefined in XML. Resource groups allow audio resources, such as streams, to be allocated according to defined limits.

Before streams are created, the audio hardware resource manager determines which resource group to use and notifies the driver of the assigned group. When the audio hardware resource manager detects a conflict, the highest priority stream rendering to the highest priority endpoint (the current default) is assigned the preferred resource group, and lower priority streams will receive the next available resource group. This process is repeated until there are no more streams or no more resources. When resources are exhausted, creation of the lowest priority stream(s) will return a failure indicating that there are insufficient resources.

When the resource group is assigned, the audio endpoint is notified of the assigned resource group. The resource XML declares which resource groups are applicable to the endpoint, in order of priority/preference, and the endpoint can be moved between the supported resource groups as needed to meet the overall system resource needs. 

With out resource groups, in releases before Windows 11, the resource management system assumes that hardware resources are limited, but those resources can be moved freely across the audio endpoints (DSP MIPS). For example the system can create up to three offload streams, one communications stream, and one speech stream at a time, across any combination of audio endpoints. When resources are declared and used, they all come from a single pool. This can be thought of as having a single resource group shared across all audio endpoints.  As there was only one resource group, there was no need to notify the driver which group was in use.

### Example Resource Group Scenario

For example if a driver has two audio endpoints and two separated paths for rendering audio, one through a DSP and one without the DSP. Chosen ahead of time, either path can be used for either endpoint, but the endpoint assigned to use the DSP has exclusive use of the DSP and all audio for the endpoint must go through the dsp. i.e. there is zero mixing audio between these two paths.

The DSP would have different resource constraints and capabilities than the endpoint without the DSP. Swapping the resources between the two endpoints would require all audio on both endpoints to be terminated, the hardware reassigned, and then audio could resume. Because the choice about whether to use the DSP or not would need to be made before any streams are created on the endpoint, the decision needs to be made outside of the driver. In the case of a conflict, two applications wanting a DSP feature at the same time, resource groups are used to decide which endpoint gets which resource.

Each resource group is created with its own set of resources, but can also optionally use the globally shared resources as well. For example, *DSPGroup* may be defined to allow for two offload streams and a host speech stream, while *NoDSPGroup* only allows for one offload stream and no host speech streams. This definition would allow for up to three offload streams to be active at one time. There could also be a system wide maximum of up to two offload streams at one time, shared across both DSPGroup and NoDSPGroup.

When a stream is created, it will be assigned to either DSPGroup or NoDSPGroup based on the type of stream being created and the priority of the stream and endpoint. If the created stream is offload it will be assigned DSPGroup, if not then it could be assigned to either DSPGroup or NoDSPGroup.

While an endpoint is assigned to a group, all streams on that endpoint are limited to the stream resources associated to the group. For example, maximum two offload streams available when an endpoint is assigned to DSPGroup.

It can be determined that an endpoint must move from one group to another group, due the priority of streams. For example, if the first offload stream was created on a speaker endpoint, and a new offload stream is being created on the headset endpoint, and there is only one DSPGroup resource set available, the DSPGroup resource will need to be reallocated from the speaker endpoint to the headset endpoint. To do this all speaker DSPGroup streams will be invalidated. DSPGroup would then be allocated to the headset endpoint and the offload stream created. After invalidation the stream recreated by the invalidated apps will encounter that offload is no longer available because they are lower priority than the existing headset endpoint offload user. NoDSPGroup will be assigned to the speaker endpoint, and streams will be limited to the speaker endpoint resource constraints, maximum six host streams possible in the system, for example.

The example described, is simplified. The system allows for any number of groups shared across any number of endpoints. For example, there could be three endpoints, sharing two capable DSP's and one limited DSP, or five endpoints sharing two DSP's and three software paths.

### Example Resource Group XML

This example XML segment defines two resource groups, *DSPGroup* and *NoDSPGroup*.

```xml
  <Limits>
    <Resource>
      <ID>DataBus</ID>
      <Consumption>8</Consumption>
    </Resource>
    <ResourceGroup Name="DSPGroup">
      <Consumption>1</Consumption>
      <Resource>
        <ID>MaxOffload</ID>
        <Consumption>3</Consumption>
      </Resource>
      <Resource>
        <ID>DspMaxLoopback</ID>
        <Consumption>1</Consumption>
      </Resource>
    </ResourceGroup>
    <ResourceGroup Name="NoDSPGroup">
      <Consumption>2</Consumption>
      <Resource>
        <ID>MaxHost</ID>
        <Consumption>2</Consumption>
      </Resource>
      <Resource>
        <ID>MaxLoopback</ID>
        <Consumption>1</Consumption>
      </Resource>
    </ResourceGroup>
  </Limits>
```

### Resource Group Allocation Behavior

- At startup, existing global resources will be allocated from the external resource manager. Then, each resource group will have a resource allocated with the external resource manager, with the count equal to the max instances of that group.

- At run time, each endpoint will be associated to only one resource group.
 
- Streams on that endpoint will only have access to the resources within the associated resource group.

- Resources from the original globally shared pool can also be used.

- When the first stream is created on an endpoint, the required endpoint resource constraint will be acquired. When the last stream is closed on the endpoint, the constraint will be released. 

- When an endpoint is assigned a resource group, it needs to be notified of the assigned resource group.

- The assigned resource group will depend upon the priority of the resource group requirements for the currently active streams, and availability.

- When the endpoint resource constraint is acquired, the streams on the endpoint are limited to the global stream resources, and the stream resources within the acquired resource group. They may not acquire a resource available in a different group.

- Resources which are part of the resource group are only used by the endpoint that is currently assigned the resource group.

- Resource groups may optionally contain additional group specific resources. A resource will be allocated from the external resource manager for each resource times the maximum instance count for the resource group. 

- When the resource group assignment is changed, all streams on the endpoint are terminated prior to the change.

- For an endpoint to move from one resource group to another resource group, all streams holding resources from the other group need to be invalidated, and upon stream creation all new resources will be acquired from the new resource group.


## Registry Key Configuration

The full path to the concurrency constraints XML file needs to be specified in the following registry key.

```inf
HKR\SYSTEM\MultiMedia\DeviceCapability\ResourceSettings\XMLConfig
```

The path is relative to the driver install. In the driver INF installation the constraint XML file needs to be copied and the following line would be added to register it with the system:

```inf
HKR,SYSTEM\MultiMedia\DeviceCapability\ResourceSettings\XMLConfig,<Name of the constraint>,,<Path to the constraint>
```

In this registry key, provide a value containing the path to the XML. It is recommended that the name of the XML file and regkey value name be unique since there is potential for other subsystems/audio devices providing their own set of constraints in XML files. The regkey can be set in the audio driver INF file.

## Example XML Constraints File

This is an example XML constraints file from the SYSVAD virtual audio driver sample.

```xml
<?xml version="1.0" encoding="utf-8"?>
<ConstraintModel>

  <Limits>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>3</Consumption>
    </Resource>
    <Resource>
      <ID>MaxTwoOffload</ID>
      <Consumption>2</Consumption>
    </Resource>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>2</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneLoopback</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>27</Consumption>
    </Resource>
  </Limits>
  
  <ExclusiveEndpoints>
    <Endpoint>
      <!-- Example of h/w id specified in phoneaudiosample.inf -->
      <HWID>Root\sysvad_PhoneAudioSample</HWID>
      <!-- Topology filter reference string-->
      <TopologyName>TopologySpeaker</TopologyName>
      <!-- KSPIN_TOPO_LINEOUT_DEST -->
      <PinId>1</PinId>
    </Endpoint>
    <Endpoint>
      <!-- Example of h/w id specified in phoneaudiosample.inf -->
      <HWID>Root\sysvad_PhoneAudioSample</HWID>
      <!-- Topology filter reference string-->
      <TopologyName>TopologyHandsetS*</TopologyName>
      <!-- KSPIN_TOPO_LINEOUT_DEST -->
      <PinId>1</PinId>
    </Endpoint>
  </ExclusiveEndpoints>

  <ExclusiveEndpoints>
    <Endpoint>
      <!-- Example of h/w id specified in phoneaudiosample.inf -->
      <HWID>Root\sysvad_PhoneAudioSample</HWID>
      <!-- Topology filter reference string-->
      <TopologyName>TopologyMicArray1</TopologyName>
      <!-- KSPIN_TOPO_MIC_ELEMENTS -->
      <PinId>0</PinId>
    </Endpoint>
    <Endpoint>
      <!-- Example of h/w id specified in phoneaudiosample.inf -->
      <HWID>Root\sysvad_PhoneAudioSample</HWID>
      <!-- Topology filter reference string-->
      <TopologyName>TopologyHandsetM*</TopologyName>
      <!-- KSPIN_TOPO_MIC_ELEMENTS -->
      <PinId>0</PinId>
    </Endpoint>
  </ExclusiveEndpoints>

  <ResourceConsumer>
    <!-- Phone call -->
    <ConsumerInfo>
      <PhoneCall>
        <CallState>Active</CallState>
      </PhoneCall>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoOffload</ID>
      <Consumption>2</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneLoopback</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>26</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- Keyword Detector -->
    <ConsumerInfo>
      <KeywordDetector />
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>2</Consumption>
    </Resource>
    <!-- Don't include MaxOneRawStreamInPhoneCall 
         so we can validate Capture stream causing
         KD release then PhoneCall releasing Capture
         and letting KD acquire -->
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to speaker, default mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeaker</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <!--Signal processing mode default-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to speaker, Communications mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeaker</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{98951333-B9CD-48B1-A0A3-FF40682D73F7}</Mode>
        <!--Signal processing mode Communications-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to speaker, Speech mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeaker</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{FC1CFC9B-B9D6-4CFA-B5E0-4BB2166878B2}</Mode>
        <!--Signal processing mode Speech-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to speaker, Notification mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeaker</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{9CF2A70B-F377-403B-BD6B-360863E0355C}</Mode>
        <!--Signal processing mode Notification-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to speaker, Media mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeaker</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{4780004E-7133-41D8-8C74-660DADD2C0EE}</Mode>
        <!--Signal processing mode Media-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to speaker, Movie mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeaker</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{B26FEB0D-EC94-477C-9494-D1AB8E753F6E}</Mode>
        <!--Signal processing mode Movie-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to speaker, raw mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeaker</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{9E90EA20-B493-4FD1-A1A8-7E1361A956CF}</Mode>
        <!--Signal processing mode raw-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>1</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to speaker, default mode, offload -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeaker</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <!--Signal processing mode default-->
        <ConnectorType>Offload</ConnectorType>
        <!-- Offload -->
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxTwoOffload</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to speaker, Media mode, Offload -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeaker</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{4780004E-7133-41D8-8C74-660DADD2C0EE}</Mode>
        <!--Signal processing mode Media-->
        <ConnectorType>Offload</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxTwoOffload</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to speaker, Movie mode, offload -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeaker</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{B26FEB0D-EC94-477C-9494-D1AB8E753F6E}</Mode>
        <!--Signal processing mode Movie-->
        <ConnectorType>Offload</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxTwoOffload</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>


  <ResourceConsumer>
    <!-- AudioStream to speaker, default mode, loopback -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeaker</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <!--Signal processing mode default-->
        <ConnectorType>Loopback</ConnectorType>
        <!-- Loopback -->
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneLoopback</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to wired headset, default mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologySpeakerHeadset</TopologyName>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <PinId>1</PinId>
        <!--Signal processing mode default-->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to wired headset, Communications mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeakerHeadset</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{98951333-B9CD-48B1-A0A3-FF40682D73F7}</Mode>
        <!--Signal processing mode Communications-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to wired headset, Speech mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeakerHeadset</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{FC1CFC9B-B9D6-4CFA-B5E0-4BB2166878B2}</Mode>
        <!--Signal processing mode Speech-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to wired headset, Notification mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeakerHeadset</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{9CF2A70B-F377-403B-BD6B-360863E0355C}</Mode>
        <!--Signal processing mode Notification-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to wired headset, Media mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeakerHeadset</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{4780004E-7133-41D8-8C74-660DADD2C0EE}</Mode>
        <!--Signal processing mode Media-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to wired headset, Movie mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeakerHeadset</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{B26FEB0D-EC94-477C-9494-D1AB8E753F6E}</Mode>
        <!--Signal processing mode Movie-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to wired headset, raw mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologySpeakerHeadset</TopologyName>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <PinId>1</PinId>
        <!--Signal processing mode raw-->
        <Mode>{9E90EA20-B493-4FD1-A1A8-7E1361A956CF}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>1</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to wired headset, default mode, offload -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologySpeakerHeadset</TopologyName>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <PinId>1</PinId>
        <!--Signal processing mode default-->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <!-- Offload -->
        <ConnectorType>Offload</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxTwoOffload</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to wired headset, Media mode, Offload -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeakerHeadset</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{4780004E-7133-41D8-8C74-660DADD2C0EE}</Mode>
        <!--Signal processing mode Media-->
        <ConnectorType>Offload</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxTwoOffload</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to wired headset, Movie mode, offload -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeakerHeadset</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{B26FEB0D-EC94-477C-9494-D1AB8E753F6E}</Mode>
        <!--Signal processing mode Movie-->
        <ConnectorType>Offload</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxTwoOffload</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>


  <ResourceConsumer>
    <!-- AudioStream to wired headset, default mode, loopback -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologySpeakerHeadset</TopologyName>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <PinId>1</PinId>
        <!--Signal processing mode default-->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <!-- Loopback -->
        <ConnectorType>Loopback</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneLoopback</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to BT speaker, raw mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyBthHfpSpeaker</TopologyName>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <PinId>1</PinId>
        <!--Signal processing mode raw-->
        <Mode>{9E90EA20-B493-4FD1-A1A8-7E1361A956CF}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>1</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to BT speaker, raw mode, offload -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyBthHfpSpeaker</TopologyName>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <PinId>1</PinId>
        <!--Signal processing mode raw-->
        <Mode>{9E90EA20-B493-4FD1-A1A8-7E1361A956CF}</Mode>
        <!-- Offload -->
        <ConnectorType>Offload</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxTwoOffload</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>1</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to BT speaker, default mode, loopback -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyBthHfpSpeaker</TopologyName>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <PinId>1</PinId>
        <!--Signal processing mode default-->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <!-- Loopback -->
        <ConnectorType>Loopback</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneLoopback</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to handset speaker, default mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyHandsetS*</TopologyName>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <PinId>1</PinId>
        <!--Signal processing mode default-->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to handset speaker, Communications mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologyHandsetS*</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{98951333-B9CD-48B1-A0A3-FF40682D73F7}</Mode>
        <!--Signal processing mode Communications-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to handset speaker, raw mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyHandsetS*</TopologyName>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <PinId>1</PinId>
        <!--Signal processing mode raw-->
        <Mode>{9E90EA20-B493-4FD1-A1A8-7E1361A956CF}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>1</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to handset speaker, default mode, loopback -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyHandsetS*</TopologyName>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <PinId>1</PinId>
        <!--Signal processing mode default-->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <!-- Loopback -->
        <ConnectorType>Loopback</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneLoopback</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from mic, default mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicIn</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode default-->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from mic, communications mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicIn</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode communications-->
        <Mode>{98951333-B9CD-48B1-A0A3-FF40682D73F7}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from mic, speech mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicIn</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode speech-->
        <Mode>{FC1CFC9B-B9D6-4CFA-B5E0-4BB2166878B2}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from mic, notification mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicIn</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode notification-->
        <Mode>{9CF2A70B-F377-403B-BD6B-360863E0355C}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from mic, raw mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicIn</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode raw-->
        <Mode>{9E90EA20-B493-4FD1-A1A8-7E1361A956CF}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>1</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from wired headset mic, default mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicHeadset</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode default-->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from wired headset mic, communications mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicHeadset</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode communications-->
        <Mode>{98951333-B9CD-48B1-A0A3-FF40682D73F7}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from wired headset mic, speech mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicHeadset</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode speech-->
        <Mode>{FC1CFC9B-B9D6-4CFA-B5E0-4BB2166878B2}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from wired headset mic, notification mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicHeadset</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode notification-->
        <Mode>{9CF2A70B-F377-403B-BD6B-360863E0355C}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from wired headset mic, raw mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicHeadset</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode raw-->
        <Mode>{9E90EA20-B493-4FD1-A1A8-7E1361A956CF}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>1</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from mic array, default mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicArray1</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode default-->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from mic array, communications mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicArray1</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode communications-->
        <Mode>{98951333-B9CD-48B1-A0A3-FF40682D73F7}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from mic array, speech mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicArray1</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode speech-->
        <Mode>{FC1CFC9B-B9D6-4CFA-B5E0-4BB2166878B2}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from mic array, notification mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicArray1</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode notification-->
        <Mode>{9CF2A70B-F377-403B-BD6B-360863E0355C}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from mic array, raw mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicArray1</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode raw-->
        <Mode>{9E90EA20-B493-4FD1-A1A8-7E1361A956CF}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>1</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from BT mic, default mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyBthHfpMic</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode default-->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from BT mic, raw mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyBthHfpMic</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode raw-->
        <Mode>{9E90EA20-B493-4FD1-A1A8-7E1361A956CF}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>1</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from handset mic, default mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyHandsetM*</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode default-->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from handset mic, communications mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyHandsetM*</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode communications-->
        <Mode>{98951333-B9CD-48B1-A0A3-FF40682D73F7}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from handset mic, speech mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyHandsetM*</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode speech-->
        <Mode>{FC1CFC9B-B9D6-4CFA-B5E0-4BB2166878B2}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from handset mic, notification mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyHandsetM*</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode notification-->
        <Mode>{9CF2A70B-F377-403B-BD6B-360863E0355C}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from handset mic, raw mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyHandsetM*</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode raw-->
        <Mode>{9E90EA20-B493-4FD1-A1A8-7E1361A956CF}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>1</Consumption>
    </Resource>
  </ResourceConsumer>

</ConstraintModel>
```
