import React from 'react';
import { motion } from 'framer-motion';
import AgentCard from './AgentCard';

const agents = [
  {
    type: 'research',
    name: 'Research Agent',
    description: 'Gathers comprehensive information and insights'
  },
  {
    type: 'writer',
    name: 'Content Writer',
    description: 'Creates engaging, well-structured content'
  },
  {
    type: 'editor',
    name: 'Editor Agent',
    description: 'Improves clarity, grammar, and flow'
  },
  {
    type: 'seo',
    name: 'SEO Optimizer',
    description: 'Optimizes content for search engines'
  },
  {
    type: 'platform',
    name: 'Platform Adapter',
    description: 'Adapts content for different platforms'
  },
  {
    type: 'qa',
    name: 'Quality Assurance',
    description: 'Ensures content meets quality standards'
  }
];

const WorkflowVisualization = ({ currentStep = -1 }) => {
  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <h3 className="text-lg font-semibold text-gray-900 mb-4">
        Multi-Agent Workflow
      </h3>
      
      <div className="space-y-4">
        {agents.map((agent, index) => (
          <div key={agent.type} className="relative">
            <AgentCard
              agent={agent}
              isActive={currentStep === index}
              isCompleted={currentStep > index}
              step={index}
            />
            
            {/* Connector line */}
            {index < agents.length - 1 && (
              <div className="flex justify-center my-2">
                <motion.div
                  initial={{ scaleY: 0 }}
                  animate={{ scaleY: currentStep > index ? 1 : 0.3 }}
                  transition={{ duration: 0.3 }}
                  className={`w-0.5 h-8 ${
                    currentStep > index ? 'bg-green-400' : 'bg-gray-300'
                  }`}
                />
              </div>
            )}
          </div>
        ))}
      </div>
      
      {currentStep >= 0 && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="mt-6 p-4 bg-blue-50 rounded-lg"
        >
          <div className="flex items-center space-x-2">
            <div className="w-2 h-2 bg-blue-500 rounded-full animate-pulse" />
            <span className="text-sm text-blue-700 font-medium">
              {currentStep < agents.length 
                ? `${agents[currentStep]?.name} is working...`
                : 'Content creation completed!'
              }
            </span>
          </div>
        </motion.div>
      )}
    </div>
  );
};

export default WorkflowVisualization;
