---
title: Touchpad Palm Deck Integration
description: Integration of a precision touchpad with the palm deck impacts the ease of use of the touchpad.
ms.assetid: CCA2894C-E8DA-4811-A8E0-21AF5D427EA7
---

# Touchpad Palm Deck Integration


Integration of a precision touchpad with the palm deck impacts the ease of use of the touchpad. Precision touchpads are designed to be natural and intuitive interface for all users. Users should able to easily identify the interaction surface, gesture in a natural and responsive fashion, and seamlessly interact with the touchpad without having to shift their focus from the screen.

## <span id="Placement"></span><span id="placement"></span><span id="PLACEMENT"></span>Placement


The optimal placement for a precision touchpad is centered between the *home keys*. For example, with an English keyboard the optimal touchpad placement is centered between the **F** and **J** keys (see *Figure 1 Optimal Horizontal Placement*). This is ideal because it is easy for users to naturally interact with the touchpad while typing, and without having to shift their focus from the screen to the touchpad.

![optimal horizontal placement](images/implementationfig10optimalhorizontalplacementzerooffset.jpg)

**Figure 1 Optimal Horizontal Placement**

## <span id="Buttons_"></span><span id="buttons_"></span><span id="BUTTONS_"></span>Buttons


A precision touchpad will have no distinct physical buttons. Precision touchpads support the click action directly (by using a click-pad or pressure-pad). Additional buttons are unnecessary and redundant. Buttons take valuable space away from the gesture surface, add cost, and clutter the palm deck and remove focus from the touchpad itself. No touchpad buttons are permitted on the palm deck or keyboard alongside a precision touchpad.

## <span id="Dimensions"></span><span id="dimensions"></span><span id="DIMENSIONS"></span>Dimensions


The optimal and recommended size for the sensor region of a precision touchpad is defined as 65mm x 105mm (see *Figure 2 Precision Touchpad Optimal Size*). These dimensions provide the optimal user experience in which a user can comfortably perform touchpad gestures and control cursor position without repeatedly clutching (lifting the finger from the touchpad surface and then repositioning it). Smaller dimensions hinder the experience of gestures such as panning, zooming, and swiping from the edge, and force the user into clutching.

![precision touchpad optimal size](images/implementationfig9optimalsize.png)

**Figure 2 Precision Touchpad Optimal Size**

The [Windows Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?LinkID=330443) requirements mandate a minimum sensor size of 32mm x 64mm for precision touchpad devices, as shown in *Figure 3 Precision Touchpad Minimum Size*.

![precision touchpad minimum size](images/implementationfig8minsize.jpg)

**Figure 3 Precision Touchpad Minimum Size**

## <span id="Alignment"></span><span id="alignment"></span><span id="ALIGNMENT"></span>Alignment


The precision touchpad is integrated so that it is level with the palm deck and there is no perceivable depth or delta. *Figure 4 Optimal Depth Offset* shows a side view of the touchpad as seen from the edge of the device. Due to manufacturing and integration tolerances, an allowance of 1.5mm is permitted for the depth offset as described in the Windows HCK. However, we recommend as close to 0mm depth offset (preferably 0-0.2mm as shown in *Figure 4 Optimal Depth Offset*) as possible, for the ideal user experience.

![optimal depth offset](images/igfig4optimaldepthoffset.png)

**Figure 4 Optimal Depth Offset**

## <span id="Coversheet_and_palm_deck_gap_"></span><span id="coversheet_and_palm_deck_gap_"></span><span id="COVERSHEET_AND_PALM_DECK_GAP_"></span>Coversheet and palm deck gap


The region (gap) between a precision touchpad and the palm deck should be minimal, but perceivable by the user. A gap no greater than 0.3mm between the touchpad and the palm deck is acceptable (see *Figure 5 Gap Between Coversheet and Palm Deck*); this provides a comfortable user experience and allows the user to perform edge gestures without shifting focus from the screen.

![gap between coversheet and palm deck ](images/igfig5gap.jpg)

**Figure 5 Gap Between Coversheet and Palm Deck**

## <span id="Edge_demarcation_"></span><span id="edge_demarcation_"></span><span id="EDGE_DEMARCATION_"></span>Edge demarcation


For implementations where the user cannot tactile-perceive the edge of the active sensor area, an edge demarcation can be used on the coversheet. Edge demarcations can be located along the boundary of the touchpad directly on the coversheet, and shall not start more than 1mm from the coversheet edge as shown in *Figure 6 Embossing Region*. Manufacturers can choose any suitable technique to make the edge demarcation perceivable to the user, such as texturing or embossing.

![embossing region ](images/igfig6embossingregion.png)

**Figure 6 Embossing Region**

## <span id="Zone_markers"></span><span id="zone_markers"></span><span id="ZONE_MARKERS"></span>Zone markers


Precision touchpads implement right-click zones. To clearly identify this region to users, zone identification markers are permitted. If implemented, zone markers shall be located in the lower center region of the precision touchpad. The zone marker shall be 10mm in height or 25% of the vertical dimension of the precision touchpad sensor region (whichever is larger, see *Figure 7 - Zone Marker for Small Precision Touchpad* and *Figure 8 Zone Marker for Large Precision Touchpad*). This delineation clearly identifies the right click region on the precision touchpad.

![- zone marker for small precision touchpad](images/igfig7zonemarkersmall.png)

**Figure 7 - Zone Marker for Small Precision Touchpad**

![zone marker for large precision touchpad](images/igfig8zonemarkerlarge.png)

**Figure 8 Zone Marker for Large Precision Touchpad**

 

 




