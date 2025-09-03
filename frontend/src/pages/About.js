import React from 'react';
import { motion } from 'framer-motion';
import { Bot, Users, Zap, Target, BarChart3, Shield, Github, ExternalLink } from 'lucide-react';

const About = () => {
  const agents = [
    {
      icon: '🔍',
      name: 'Research Agent',
      description: 'Conducts comprehensive research, gathers facts, statistics, and current trends from reliable sources.',
      capabilities: ['Web search and data collection', 'Fact verification', 'Trend analysis', 'Source validation']
    },
    {
      icon: '✍️',
      name: 'Content Writer Agent',
      description: 'Creates engaging, well-structured content based on research findings and user requirements.',
      capabilities: ['Creative writing', 'Audience adaptation', 'Content structuring', 'Narrative development']
    },
    {
      icon: '📝',
      name: 'Editor Agent',
      description: 'Reviews and improves content for clarity, grammar, flow, and overall readability.',
      capabilities: ['Grammar correction', 'Style improvement', 'Flow optimization', 'Readability enhancement']
    },
    {
      icon: '🎯',
      name: 'SEO Optimizer Agent',
      description: 'Optimizes content for search engines while maintaining quality and readability.',
      capabilities: ['Keyword integration', 'Meta tag generation', 'Content structure optimization', 'SEO best practices']
    },
    {
      icon: '📱',
      name: 'Platform Adapter Agent',
      description: 'Adapts content for different platforms with specific formatting and optimization.',
      capabilities: ['Platform-specific formatting', 'Character limit compliance', 'Hashtag optimization', 'Engagement strategies']
    },
    {
      icon: '✅',
      name: 'Quality Assurance Agent',
      description: 'Performs final quality checks ensuring all content meets the highest standards.',
      capabilities: ['Quality scoring', 'Compliance checking', 'Final approval', 'Improvement recommendations']
    }
  ];

  const technologies = [
    {
      name: 'CrewAI',
      description: 'Multi-agent orchestration framework',
      logo: '🤖'
    },
    {
      name: 'LangChain',
      description: 'LLM integration and prompt management',
      logo: '🔗'
    },
    {
      name: 'OpenAI GPT',
      description: 'Primary language model for content generation',
      logo: '🧠'
    },
    {
      name: 'Google Gemini',
      description: 'Alternative LLM with free tier support',
      logo: '💎'
    },
    {
      name: 'React',
      description: 'Modern frontend framework',
      logo: '⚛️'
    },
    {
      name: 'Tailwind CSS',
      description: 'Utility-first CSS framework',
      logo: '🎨'
    }
  ];

  const features = [
    {
      icon: Bot,
      title: 'Multi-Agent Collaboration',
      description: 'Six specialized AI agents working together for optimal results'
    },
    {
      icon: Zap,
      title: 'Lightning Fast',
      description: 'Generate high-quality content in under 60 seconds'
    },
    {
      icon: Target,
      title: 'SEO Optimized',
      description: 'Automatically optimized for search engines and conversions'
    },
    {
      icon: Users,
      title: 'Platform Specific',
      description: 'Content adapted for Twitter, LinkedIn, blogs, and more'
    },
    {
      icon: BarChart3,
      title: 'Quality Assured',
      description: 'Built-in quality checks and approval workflows'
    },
    {
      icon: Shield,
      title: 'Reliable Results',
      description: 'Consistent, professional-grade content every time'
    }
  ];

  return (
    <div className="max-w-7xl mx-auto">
      {/* Hero Section */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center py-20"
      >
        <h1 className="text-4xl font-bold text-gray-900 mb-6">
          About Smart Content Pipeline
        </h1>
        <p className="text-xl text-gray-600 max-w-3xl mx-auto mb-8">
          An innovative AI multi-agent system designed for the CODING NINJAS assignment, 
          demonstrating how specialized AI agents can collaborate to solve real-world 
          content creation challenges.
        </p>
        <div className="flex justify-center space-x-4">
          <a
            href="https://github.com/zaidiqbalcode/ai-multi-agent-systems"
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center space-x-2 bg-gray-900 hover:bg-gray-800 text-white font-semibold py-3 px-6 rounded-lg transition-colors duration-200"
          >
            <Github className="h-5 w-5" />
            <span>View on GitHub</span>
          </a>
          <a
            href="/create"
            className="flex items-center space-x-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded-lg transition-colors duration-200"
          >
            <ExternalLink className="h-5 w-5" />
            <span>Try Demo</span>
          </a>
        </div>
      </motion.div>

      {/* Problem Statement */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.2 }}
        className="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-xl p-8 mb-16"
      >
        <h2 className="text-2xl font-bold text-gray-900 mb-4">Problem Statement</h2>
        <p className="text-gray-700 mb-4">
          In today's digital landscape, content creators and marketing teams face the challenge of 
          producing high-quality, platform-specific content at scale. Creating content that is 
          optimized for different platforms while maintaining consistency, accuracy, and engagement 
          is time-consuming and requires diverse expertise.
        </p>
        <h3 className="text-lg font-semibold text-gray-900 mb-2">Why Multi-Agent AI?</h3>
        <ul className="space-y-2 text-gray-700">
          <li><strong>Specialization:</strong> Different agents focus on specific expertise areas</li>
          <li><strong>Quality Assurance:</strong> Multiple layers of review and improvement</li>
          <li><strong>Scalability:</strong> Handle multiple content requests simultaneously</li>
          <li><strong>Consistency:</strong> Maintain quality standards across all content</li>
          <li><strong>Efficiency:</strong> Parallel processing reduces creation time</li>
        </ul>
      </motion.div>

      {/* Agent Details */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.3 }}
        className="mb-16"
      >
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          Meet Our AI Agents
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {agents.map((agent, index) => (
            <motion.div
              key={agent.name}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.1 * index }}
              className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow duration-200"
            >
              <div className="text-4xl mb-4 text-center">{agent.icon}</div>
              <h3 className="text-lg font-semibold text-gray-900 mb-2 text-center">
                {agent.name}
              </h3>
              <p className="text-gray-600 mb-4 text-sm">
                {agent.description}
              </p>
              <div>
                <h4 className="text-sm font-medium text-gray-900 mb-2">Key Capabilities:</h4>
                <ul className="space-y-1">
                  {agent.capabilities.map((capability, capIndex) => (
                    <li key={capIndex} className="text-xs text-gray-600 flex items-center">
                      <span className="w-1 h-1 bg-blue-500 rounded-full mr-2"></span>
                      {capability}
                    </li>
                  ))}
                </ul>
              </div>
            </motion.div>
          ))}
        </div>
      </motion.div>

      {/* Technology Stack */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.4 }}
        className="mb-16"
      >
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          Technology Stack
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {technologies.map((tech, index) => (
            <motion.div
              key={tech.name}
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ delay: 0.1 * index }}
              className="bg-white rounded-lg shadow-md p-6 text-center hover:shadow-lg transition-shadow duration-200"
            >
              <div className="text-3xl mb-3">{tech.logo}</div>
              <h3 className="font-semibold text-gray-900 mb-2">{tech.name}</h3>
              <p className="text-sm text-gray-600">{tech.description}</p>
            </motion.div>
          ))}
        </div>
      </motion.div>

      {/* Features */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.5 }}
        className="mb-16"
      >
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          Key Features
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {features.map((feature, index) => (
            <motion.div
              key={feature.title}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.1 * index }}
              className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow duration-200"
            >
              <feature.icon className="h-12 w-12 text-blue-600 mb-4" />
              <h3 className="text-lg font-semibold text-gray-900 mb-2">
                {feature.title}
              </h3>
              <p className="text-gray-600">
                {feature.description}
              </p>
            </motion.div>
          ))}
        </div>
      </motion.div>

      {/* Assignment Context */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.6 }}
        className="bg-white rounded-lg shadow-md p-8 mb-16"
      >
        <h2 className="text-2xl font-bold text-gray-900 mb-6">
          CODING NINJAS Assignment Context
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div>
            <h3 className="text-lg font-semibold text-gray-900 mb-4">Assignment Requirements</h3>
            <ul className="space-y-2 text-gray-700">
              <li>✅ Build an AI Multi-Agent Based Project</li>
              <li>✅ Demonstrate meaningful real-world application</li>
              <li>✅ Show effective agent collaboration</li>
              <li>✅ Document tools and frameworks used</li>
              <li>✅ Explain LLM selection and reasoning</li>
              <li>✅ Provide complete GitHub repository</li>
              <li>✅ Include setup and run instructions</li>
            </ul>
          </div>
          <div>
            <h3 className="text-lg font-semibold text-gray-900 mb-4">Project Highlights</h3>
            <ul className="space-y-2 text-gray-700">
              <li>🎯 Solves real content creation challenges</li>
              <li>🤖 Six specialized AI agents collaborating</li>
              <li>⚡ Fast, efficient content generation</li>
              <li>🔧 Multiple LLM options (OpenAI, Google)</li>
              <li>🌐 Modern React frontend interface</li>
              <li>📱 Platform-specific optimizations</li>
              <li>✨ Quality assurance built-in</li>
            </ul>
          </div>
        </div>
      </motion.div>

      {/* LLM Selection */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.7 }}
        className="bg-gradient-to-r from-green-50 to-blue-50 rounded-xl p-8"
      >
        <h2 className="text-2xl font-bold text-gray-900 mb-6">LLM Selection Strategy</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div>
            <h3 className="text-lg font-semibold text-gray-900 mb-4">Primary: OpenAI GPT-4</h3>
            <p className="text-gray-700 mb-4">
              Chosen for superior content quality, complex reasoning, and excellent creative writing capabilities.
            </p>
            <ul className="space-y-1 text-sm text-gray-600">
              <li>• High-quality, creative output</li>
              <li>• Excellent instruction following</li>
              <li>• Strong content generation</li>
              <li>• Reliable performance</li>
            </ul>
          </div>
          <div>
            <h3 className="text-lg font-semibold text-gray-900 mb-4">Free Alternative: Google Gemini</h3>
            <p className="text-gray-700 mb-4">
              Free tier option providing good performance for content tasks with reasonable quality output.
            </p>
            <ul className="space-y-1 text-sm text-gray-600">
              <li>• Free tier available</li>
              <li>• Fast response times</li>
              <li>• Good multilingual support</li>
              <li>• Cost-effective solution</li>
            </ul>
          </div>
        </div>
      </motion.div>
    </div>
  );
};

export default About;
