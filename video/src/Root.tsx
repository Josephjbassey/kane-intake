import React from 'react';
import { Composition } from 'remotion';
import { WalkthroughComposition } from './WalkthroughComposition';
import screensData from '../screens.json';

export const Root: React.FC = () => {
  const screens = screensData.screens;
  const transitionDuration = 30;
  const totalFrames =
    screens.reduce((acc, s) => acc + s.durationInFrames, 0) -
    (screens.length - 1) * transitionDuration;

  return (
    <Composition
      id="WalkthroughComposition"
      component={WalkthroughComposition}
      durationInFrames={totalFrames}
      fps={30}
      width={1920}
      height={1080}
    />
  );
};
