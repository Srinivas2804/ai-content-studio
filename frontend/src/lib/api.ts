import axios from 'axios'

const api = axios.create({ baseURL: '/api' })

export interface Job {
  id: string
  title: string
  content_type: string
  status: 'queued' | 'processing' | 'completed' | 'failed'
  progress: number
  formats: FormatResult[]
  created_at: string
  updated_at: string
  user_id: string
}

export interface FormatResult {
  format: string
  status: string
  content: string | null
  word_count: number | null
  created_at: string | null
}

export interface Analytics {
  total_jobs: number
  completed_jobs: number
  total_formats_generated: number
  formats_this_month: number
  avg_completion_time_minutes: number
  top_format: string
  jobs_by_status: Record<string, number>
  monthly_usage: { month: string; jobs: number; formats: number }[]
}

export const getJobs = () => api.get<Job[]>('/jobs').then(r => r.data)
export const getJob = (id: string) => api.get<Job>(`/jobs/${id}`).then(r => r.data)
export const createJob = (data: any) => api.post<Job>('/jobs', data).then(r => r.data)
export const deleteJob = (id: string) => api.delete(`/jobs/${id}`).then(r => r.data)
export const getAnalytics = () => api.get<Analytics>('/analytics/summary').then(r => r.data)