import React from 'react';
import { interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';

interface TextOverlayProps {
  title: string;
  description: string;
  currentScreen: number;
  totalScreens: number;
}

export const TextOverlay: React.FC<TextOverlayProps> = ({
  title,
  description,
  currentScreen,
  totalScreens,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const titleProgress = spring({
    frame,
    fps,
    config: { damping: 15, stiffness: 120 },
  });

  const titleOpacity = interpolate(titleProgress, [0, 1], [0, 1]);
  const titleY = interpolate(titleProgress, [0, 1], [-20, 0]);

  const descProgress = spring({
    frame: frame - 10,
    fps,
    config: { damping: 15, stiffness: 100 },
  });
  const descOpacity = interpolate(descProgress, [0, 1], [0, 1]);
  const descY = interpolate(descProgress, [0, 1], [20, 0]);

  const progressPct = ((currentScreen) / totalScreens) * 100;

  return (
    <div
      style={{
        position: 'absolute',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        pointerEvents: 'none',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'space-between',
        padding: '40px 60px',
      }}
    >
      {/* Top Bar */}
      <div
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          background: 'rgba(15, 23, 42, 0.85)',
          backdropFilter: 'blur(12px)',
          padding: '16px 28px',
          borderRadius: '16px',
          border: '1px solid rgba(71, 85, 105, 0.5)',
          opacity: titleOpacity,
          transform: `translateY(${titleY}px)`,
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
          <div
            style={{
              width: '40px',
              height: '40px',
              borderRadius: '8px',
              background: '#10b981',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              color: 'white',
              fontWeight: 800,
              fontSize: '22px',
              fontFamily: 'system-ui, sans-serif',
            }}
          >
            K
          </div>
          <div>
            <h1
              style={{
                color: '#f8fafc',
                fontSize: '24px',
                fontWeight: 700,
                margin: 0,
                fontFamily: 'system-ui, sans-serif',
              }}
            >
              {title}
            </h1>
            <p
              style={{
                color: '#94a3b8',
                fontSize: '15px',
                margin: 0,
                marginTop: '4px',
                fontFamily: 'system-ui, sans-serif',
              }}
            >
              {description}
            </p>
          </div>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
          <div
            style={{
              background: 'rgba(30, 41, 59, 0.8)',
              padding: '8px 16px',
              borderRadius: '8px',
              border: '1px solid rgba(100, 116, 139, 0.4)',
              color: '#34d399',
              fontSize: '14px',
              fontWeight: 600,
              fontFamily: 'system-ui, monospace',
            }}
          >
            Kane CLI Closed-Loop
          </div>
          <div
            style={{
              color: '#cbd5e1',
              fontSize: '15px',
              fontWeight: 600,
              fontFamily: 'system-ui, monospace',
            }}
          >
            Step {currentScreen} / {totalScreens}
          </div>
        </div>
      </div>

      {/* Bottom Progress Bar */}
      <div
        style={{
          width: '100%',
          height: '6px',
          background: 'rgba(30, 41, 59, 0.6)',
          borderRadius: '3px',
          overflow: 'hidden',
          border: '1px solid rgba(71, 85, 105, 0.4)',
        }}
      >
        <div
          style={{
            height: '100%',
            width: `${progressPct}%`,
            background: 'linear-gradient(90deg, #10b981, #3b82f6, #a855f7)',
            transition: 'width 0.3s ease',
          }}
        />
      </div>
    </div>
  );
};
