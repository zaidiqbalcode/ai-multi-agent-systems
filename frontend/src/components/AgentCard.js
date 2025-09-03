import React from 'react';
import { motion } from 'framer-motion';

const AgentCard = ({ agent, isActive, isCompleted, step }) => {
  const getStatusColor = () => {
    if (isCompleted) return 'bg-green-100 border-green-300 text-green-800';
    if (isActive) return 'bg-blue-100 border-blue-300 text-blue-800';
    return 'bg-gray-100 border-gray-300 text-gray-600';
  };

  const getIcon = () => {
    switch (agent.type) {
      case 'research':
        return '🔍';
      case 'writer':
        return '✍️';
      case 'editor':
        return '📝';
      case 'seo':
        return '🎯';
      case 'platform':
        return '📱';
      case 'qa':
        return '✅';
      default:
        return '🤖';
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: step * 0.1 }}
      className={`p-4 rounded-lg border-2 transition-all duration-300 ${getStatusColor()}`}
    >
      <div className="flex items-center space-x-3">
        <div className="text-2xl">{getIcon()}</div>
        <div className="flex-1">
          <h3 className="font-semibold text-sm">{agent.name}</h3>
          <p className="text-xs opacity-75 mt-1">{agent.description}</p>
        </div>
        <div className="flex-shrink-0">
          {isCompleted && (
            <div className="w-6 h-6 bg-green-500 rounded-full flex items-center justify-center">
              <svg className="w-3 h-3 text-white" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
              </svg>
            </div>
          )}
          {isActive && !isCompleted && (
            <div className="w-6 h-6 bg-blue-500 rounded-full flex items-center justify-center">
              <div className="w-2 h-2 bg-white rounded-full animate-pulse" />
            </div>
          )}
        </div>
      </div>
    </motion.div>
  );
};

export default AgentCard;
