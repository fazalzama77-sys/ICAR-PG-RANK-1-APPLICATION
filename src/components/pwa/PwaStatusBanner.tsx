import React, { useState } from 'react';
import { WifiOff, RefreshCw, X } from 'lucide-react';
import { usePwa } from '../../hooks/usePwa';

export const PwaStatusBanner: React.FC = () => {
  const { isOnline, needRefresh } = usePwa();
  const [dismissOfflineAlert, setDismissOfflineAlert] = useState(false);

  return (
    <>
      {/* Offline Alert Banner */}
      {!isOnline && !dismissOfflineAlert && (
        <div className="bg-amber-600 text-white px-4 py-2 text-xs flex items-center justify-between shadow-inner">
          <div className="flex items-center space-x-2">
            <WifiOff className="w-4 h-4 animate-pulse shrink-0" />
            <span>
              <strong>Offline Mode Active:</strong> You are currently disconnected from the internet. All questions, CBT mock engines, timers, and test scoring remain 100% functional.
            </span>
          </div>
          <button
            onClick={() => setDismissOfflineAlert(true)}
            className="text-amber-200 hover:text-white ml-2 p-1"
            title="Dismiss notification"
          >
            <X className="w-3.5 h-3.5" />
          </button>
        </div>
      )}

      {/* New Service Worker Update Ready */}
      {needRefresh && (
        <div className="bg-indigo-600 text-white px-4 py-2 text-xs flex items-center justify-between shadow-md">
          <div className="flex items-center space-x-2">
            <RefreshCw className="w-4 h-4 animate-spin shrink-0" />
            <span>A new version of the CBT engine is cached and ready!</span>
          </div>
          <button
            onClick={() => window.location.reload()}
            className="bg-white text-indigo-700 font-semibold px-2.5 py-1 rounded text-xs hover:bg-indigo-50 transition-colors shadow-xs"
          >
            Reload to Update
          </button>
        </div>
      )}
    </>
  );
};
