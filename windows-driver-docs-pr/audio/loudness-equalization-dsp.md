---
title: Loudness Equalization DSP
description: Loudness Equalization DSP
ms.date: 06/15/2022
---

# Loudness Equalization DSP

The loudness equalization DSP ensures that the volume level across different sources of audio signal stays constant. A TV program, for example, might be at just the right volume level whereas the commercial breaks within the program can vary widely in volume. This requires users to adjust the volume setting accordingly. Some of today's expensive HD-capable TVs can equalize volume so that the sound stays at a somewhat constant level. That works well if you rely on your TV for sound playback, but most home theater and home audio enthusiasts connect the TV audio directly to their stereo sound systems. In addition, today's loudness equalization solutions are often not effective for different audio content and sources.

Versions of Windows with this audio effect can maintain a more uniform perceived loudness across different digital audio files or sources than earlier Windows technologies. This means that loudness always stays within a specified range, even for different digital signals.

Loudness equalization is ideal, for example, for watching a movie at night. It makes it easier to hear the quieter parts of the movie while limiting the maximum loudness to a level that is considerate of others. Loudness equalization also improves the listening experience in noisy playback settings, by making the quiet parts of the content loud enough to be audible without creating disturbingly loud peak volumes.

Loudness and intensity are different ways of quantifying audio levels.

- Loudness, in its technical sense, refers to the listener's perception of an audio signal's volume.
- Intensity (volume and level) is the externally measured power of an audio signal.

Two signals of the same intensity with different time structure or frequency content can have substantially different loudness levels. This leads to the common experience where some content sounds much louder than other content with the same intensity simply because of differences in the source material and the way in which the content was recorded. Furthermore, different content standards—such as digital versus analog TV)—could have different intensity levels for the same content. As a result, the perceived level of audio content can vary widely, from nearly inaudible in a moderately quiet listening environment to loud enough to be uncomfortable.

Loudness equalization simulates human hearing to accurately measure the loudness—as opposed to intensity—of an audio source. It then uses dynamic gain adjustment to keep the loudness of different sources more nearly constant. Loudness equalization can thus affect both dynamic range and peak loudness. Windows Vista uses single-pass loudness equalization, which calculates loudness on a block-by-block basis. A block corresponds to the critical band resolution of a human year. Single-pass loudness equalization adjusts the gain with a fast attack and slow decay—just as many wideband compressors do—to tightly control the peak loudness of a signal while maintaining the local dynamics.

- Fast attack means that relatively loud signals have their gain rapidly reduced to control the loudest signal that is presented to the listener.

- Slow decay means that, when an audio signal reaches a peak but does not sustain that level, the gain following the peak is slowly increased.

Single-pass loudness equalization equalizes long-term level changes somewhat, but preserves the signal's short-term dynamics. The loudness equalization is not full, and the technique deliberately preserves some sense of louder versus softer across different material.
