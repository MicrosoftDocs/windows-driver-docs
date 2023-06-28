---
title: Camera Profile V2 architectural overview
description: This article provides a Camera Profile V2 architectural overview.
ms.date: 06/08/2023
---

# Architectural overview (Camera Profile V2)

The current Camera Profile is all stored on the individual Device Interface nodes. If the KS API is used it's stored as a DEVPKEY property, while INF version is directly updated as a set of registry entries.

This was necessary in the past since there was no centralized authority to manage all the profile information. With Windows 10 1607 and the introduction of Windows Camera Frame Server service (herein referred to as Frame Server), we can now use the Frame Server to handle the publication and storage of camera profiles.

## Media Type Filter profile definition

One of the major challenge with Camera Profile 1507 schema is that its media type centric. This requires publishers to declare explicitly every media type that is supported on each of the pin for each profile.

When each pin exposes dozens of media type, a profile that excludes one or two media types from the list, is required to declare each supported media type. This results in a large list of media types. This adds overhead for authoring and increases the potential for mistakes.

Based on partner feedback, most profiles are constrained on processing power; bandwidth or specific sensor modes. Such constraints are easy to express in terms of range of media information: resolution, frame rate and/or color space (for example, four CC value).

Camera Profile V2 defines a new "language" for Media Type Filter. A Media Type Filter describes a range of media type information. Because the Media Type Filter is a collection of string tokens, it's extensible so more range information can be added in the future.

## Related articles

[Camera Profile V2 developer specification](camera-profile-v2-specification.md)
