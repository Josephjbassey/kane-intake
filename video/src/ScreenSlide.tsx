import React from 'react';
import { Img, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from 'remotion';
import { TextOverlay } from './components/TextOverlay';

interface ScreenSlideProps {
  imageSrc: string;
  title: string;
  description: string;
  screenIndex: number;
  totalScreens: number;
}

export const ScreenSlide: React.FC<ScreenSlideProps> = ({
  imageSrc,
  title,
  description,
  screenIndex,
  totalScreens,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Subtle zoom-in animation
  const scale = spring({
    frame,
    fps,
    config: { damping: 20, stiffness: 80, mass: 1 },
  });

  const zoomFactor = interpolate(scale, [0, 1], [0.95, 1.0]);
  const opacity = interpolate(frame, [0, 15], [0, 1], { extrapolateRight: 'clamp' });

  return (
    <div
      style={{
        width: '100%',
        height: '100%',
        backgroundColor: '#0f172a',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        position: 'relative',
        overflow: 'hidden',
      }}
    >
      {/* Background glow */}
      <div
        style={{
          position: 'absolute',
          width: '800px',
          height: '800px',
          borderRadius: '50%',
          background: 'radial-gradient(circle, rgba(59, 130, 246, 0.12) 0%, rgba(15, 23, 42, 0) 70%)',
          top: '20%',
          left: '25%',
          pointerEvents: 'none',
        }}
      />

      {/* Screen Screenshot Container */}
      <div
        style={{
          width: '1800px',
          height: '880px',
          marginTop: '60px',
          borderRadius: '16px',
          overflow: 'hidden',
          boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.7)',
          border: '1px solid rgba(71, 85, 105, 0.6)',
          transform: `scale(${zoomFactor})`,
          opacity,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          backgroundColor: '#1e293b',
        }}
      >
        <Img
          src={staticFile(imageSrc)}
          style={{
            width: '100%',
            height: '100%',
            objectFit: 'contain',
          }}
        />
      </div>

      {/* Contextual Text & Progress Overlay */}
      <TextOverlay
        title={title}
        description={description}
        currentScreen={screenIndex}
        totalScreens={totalScreens}
      />
    </div>
  );
};
