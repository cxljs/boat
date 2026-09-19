/**
 * Main type export file - central hub for all Boat types
 */

export * from "./boat";
export * from "./eval";

// Import core types from boat for convenience
import type {
  Entity,
  AgentInfo,
  OrchestratorInfo,
  SessionInfo,
  Message,
  StreamEvent
} from "./boat";

// Application state types
export interface AppState {
  entities: Entity[];
  agents: AgentInfo[];
  orchestrators: OrchestratorInfo[];
  selectedEntity?: Entity;
  currentSession?: SessionInfo;
  isLoading: boolean;
  error?: string;
}

// Chat UI state
export interface ChatState {
  messages: Message[];
  isStreaming: boolean;
  streamEvents: StreamEvent[];
}

// Re-export specific types for external usage
export type {
  Entity,
  AgentInfo,
  OrchestratorInfo,
  SessionInfo,
  Message,
  StreamEvent,
  RunEntityRequest,
  HealthResponse
} from "./boat";