import React from 'react';
import { TransitionSeries, linearTiming } from '@remotion/transitions';
import { fade } from '@remotion/transitions/fade';
import { ScreenSlide } from './ScreenSlide';
import screensData from '../screens.json';

export const WalkthroughComposition: React.FC = () => {
  const screens = screensData.screens;
  const transitionDuration = 30; // 1 second fade transition

  return (
    <TransitionSeries>
      {screens.map((screen, idx) => {
        const isLast = idx === screens.length - 1;
        return (
          <React.Fragment key={screen.id}>
            <TransitionSeries.Sequence durationInFrames={screen.durationInFrames}>
              <ScreenSlide
                imageSrc={screen.imagePath}
                title={screen.title}
                description={screen.description}
                screenIndex={idx + 1}
                totalScreens={screens.length}
              />
            </TransitionSeries.Sequence>
            {!isLast && (
              <TransitionSeries.Transition
                presentation={fade()}
                timing={linearTiming({ durationInFrames: transitionDuration })}
              />
            )}
          </React.Fragment>
        );
      })}
    </TransitionSeries>
  );
};
