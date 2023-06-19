---
title: Camera Profile V2 developer specification
description: This article provides an overview of the Camera Profile V2 developer specification.
ms.date: 06/08/2023
---

# Camera Profile V2 developer specification

This article provides an overview of the Camera Profile V2 developer specification.

## Contents

[Camera Profile V2 developer specification overview](#overview)

[Architectural overview](camera-profile-v2-architectural-overview.md)

[Detailed design for IHVs and OEMs](camera-profile-v2-detailed-design-for-ihvs-and-oems.md)

[Sample profile declaration](camera-profile-v2-sample-profile-declaration.md)

[Legacy profile](camera-profile-v2-legacy-profile.md)

[Sensor group generation](camera-profile-v2-sensor-group-generation.md)

[Sensor group configuration](camera-profile-v2-sensor-group-configuration.md)

[Device MFT support](camera-profile-v2-device-mft-support.md)

[Sensor group transforms](camera-profile-v2-sensor-group-transforms.md)

[Constraint match logic](camera-profile-v2-constraint-match-logic.md)

[Detailed design for ISVs](camera-profile-v2-detailed-design-for-isvs.md)

[Profile discovery](camera-profile-v2-profile-discovery.md)

[Interfaces and interactions](camera-profile-v2-interfaces-and-interactions.md)

[Sample code](camera-profile-v2-sample-code.md)

## Overview

With Windows 10 1507, Camera Profile (herein referred to as Camera Profile 1507) support was added to allow IHV/OEMs to describe to the platform and to the developers the hardware limitation of the camera(s) available on the device.

These limitations ranged from concurrent use of cameras, limited media types based on concurrent use, and/or limited media types based on combinations of streams on one or more cameras.

However, the generation and consumption of these descriptive limitations proved to be cumbersome and error prone. Camera Profile V2 is an extension to the original spec to address many of the pain points discovered in the original Camera Profile specification.

V2 will also attempt to address the difficulty in consumption of the Camera Profiles by ISVs by using the support of Frame Server that is now available on Windows 10 platforms.

In Camera Profile 1507, there were two ways for Camera Profiles to be defined for any given machine:

- KS API

- INF Override

The KS API is a driver initialization time API to publish or update any profile information. To maintain backwards compatibility, these APIs are re-routed to support to Camera Profile V2 schema described below.

The INF Override was intended as a means to provide an override mechanism for a common driver set. For example, an IHV creates a single binary driver that initializes the Camera Profile based on a reference implementation, then produces multiple INFs that overrides the reference profiles with SKU specific profiles.

These INF Overrides will also be rerouted internally to the Camera Profile V2 to maintain backwards compatibility.

There are two major goals for this design:

- Simplify Publishing of Camera Profiles

- Simplify Consumption of Camera Profiles

For publishing of camera profiles, the requirements to declare profiles will be simplified to reduce the amount of code/INF that IHV/OEMs have to write.

For consumption of camera profiles, we'll use Frame Server's context management to alter pin/media types during initialization of each context to match the available profile information.

## Terminology

| Term | Definition |
|--|--|
| Profile Constraint | A set of constraints that applies to the entire profile. |
| LRS | Profile Constraint tag: Represents Lock Resolution. |
| LFR | Profile Constraint tag: Represents Lock Frame Rate. |
| LST | Profile Constraint tag: Represents Lock Subtype. |
| DIS | Profile Constraint tag: Disable Profile. |
| UAR | Profile Constraint tag: Unlock Aspect Ratio. |
| Filter Set | A Profile Schema entry representing a set of Filters. |
| Filter | A Profile Schema entry representing a combination of Filter Attribute, Filter Comparison Operator and Filter Value. |
| Filter Attribute | Represents one of the attributes available in an MF Media Type. Currently only Resolution, Frame Rate and Subtype are defined:<br><br>RES – Resolution<br><br>FRT – Frame Rate<br><br>SUT – Subtype |
| Filter Comparison Operator | Represents the comparison operation for a Resolution, Frame Rate or Subtype. |
| Filter Value | Value of the Filter Attribute. The representation of each varies based on the Filter Attribute. See below. |
