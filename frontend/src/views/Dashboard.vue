<template>
  <div class="app-container">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
      <h2>🕷️ JobRadar 爬虫控制台</h2>

      <div>
        <span style="margin-right: 15px; color: #666;">
          欢迎回来, {{ userStore.username }}
        </span>
        <el-button type="danger" plain @click="handleLogout">
          退出登录
        </el-button>
      </div>
    </div>

    <div class="header-actions">
      <el-button type="primary" size="large" @click="fetchTasks">
        🔄 刷新列表
      </el-button>
      <el-button type="success" size="large" @click="dialogVisible = true">
        ➕ 新建任务
      </el-button>
    </div>

    <el-table :data="tasks" style="width: 100%; margin-top: 20px" border v-loading="loading">
      <el-table-column prop="id" label="ID" width="60" />
      <el-table-column prop="name" label="任务名称" width="180">
        <template #default="scope"><strong>{{ scope.row.name }}</strong></template>
      </el-table-column>
      <el-table-column prop="target_url" label="目标 URL" show-overflow-tooltip />
      <el-table-column prop="status" label="状态" width="120">
        <template #default="scope">
          <el-tag :type="getStatusType(scope.row.status)">{{ scope.row.status }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="frequency" label="频率" width="100" />
      <el-table-column label="操作" width="220">
        <template #default="scope">
          <el-button size="small" type="primary" plain @click="handleViewResults(scope.row.id)">
            👀 查看数据
          </el-button>
          <el-button size="small" type="danger" plain @click="handleDelete(scope.row.id)">
            删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-dialog v-model="dialogVisible" title="新建爬虫任务" width="500px">
      <el-form :model="createForm" label-width="100px">
        <el-form-item label="任务名称">
          <el-input v-model="createForm.name" placeholder="例如：Quotes 每日抓取" />
        </el-form-item>
        <el-form-item label="目标 URL">
          <el-input v-model="createForm.target_url" placeholder="https://..." />
        </el-form-item>
        <el-form-item label="执行频率">
          <el-select v-model="createForm.frequency" placeholder="选择频率">
            <el-option label="单次执行" value="once" />
            <el-option label="每天一次" value="daily" />
            <el-option label="每周一次" value="weekly" />
          </el-select>
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="dialogVisible = false">取消</el-button>
          <el-button type="primary" @click="handleCreate">立即创建并运行</el-button>
        </span>
      </template>
    </el-dialog>

    <el-dialog v-model="resultDialogVisible" title="抓取结果 (MongoDB Data)" width="800px">
      <el-table v-if="spiderResults.length > 0" :data="spiderResults" border height="400">
        <el-table-column prop="text" label="名言内容" show-overflow-tooltip />
        <el-table-column prop="author" label="作者" width="150" />
        <el-table-column prop="tags" label="标签">
          <template #default="scope">
            <el-tag size="small" v-for="tag in scope.row.tags" :key="tag" style="margin-right:5px">
              {{ tag }}
            </el-tag>
          </template>
        </el-table-column>
      </el-table>
      <el-empty v-else description="暂无数据或数据加载中" />
    </el-dialog>

  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import request from '../utils/request'
import { useUserStore } from '../stores/user'
import { useRouter } from 'vue-router'
import { ElMessage, ElMessageBox } from 'element-plus'

// --- 变量定义 ---
const tasks = ref([])
const loading = ref(false)
const dialogVisible = ref(false)
const resultDialogVisible = ref(false)
const spiderResults = ref([])

const userStore = useUserStore()
const router = useRouter()

const createForm = reactive({
  name: '',
  target_url: '',
  frequency: 'daily'
})

// --- 方法 ---
const fetchTasks = async () => {
  loading.value = true
  try {
    const response = await request.get('/api/tasks/')
    tasks.value = response.data
  } catch (error) {
    ElMessage.error('获取任务列表失败')
  } finally {
    loading.value = false
  }
}

const handleCreate = async () => {
  try {
    await request.post('/api/tasks/', createForm)
    ElMessage.success('任务创建成功！')
    dialogVisible.value = false
    fetchTasks()
  } catch (error) {
    ElMessage.error('创建任务失败')
  }
}

const handleDelete = async (id) => {
  try {
    await ElMessageBox.confirm('确定要删除这个任务吗？', '提示', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    })
    await request.delete(`/api/tasks/${id}/`)
    ElMessage.success('删除成功')
    fetchTasks()
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败')
    }
  }
}

const handleViewResults = async (id) => {
  try {
    const response = await request.get(`/api/tasks/${id}/results/`)
    spiderResults.value = response.data
    resultDialogVisible.value = true
  } catch (error) {
    ElMessage.error('获取数据失败')
  }
}

const handleLogout = () => {
  userStore.logout()
  router.push('/login')
}

const getStatusType = (status) => {
  const map = {
    'PENDING': 'info',
    'RUNNING': 'warning',
    'COMPLETED': 'success',
    'FAILED': 'danger'
  }
  return map[status] || 'info'
}

// --- 生命周期 ---
onMounted(() => {
  fetchTasks()
})
</script>

<style scoped>
.app-container {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}
.header-actions {
  margin-bottom: 20px;
}
</style>
